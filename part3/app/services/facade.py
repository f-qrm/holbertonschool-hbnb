import uuid
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from datetime import datetime, timezone
from app.persistence.repository import SQLAlchemyRepository
from app.services.repositories. user_repo import UserRepository
from app.services.repositories. amenity_repo import AmenityRepository


class HBnBFacade:
    def __init__(self):
        self.user_repository = UserRepository()  # Switched to SQLAlchemyRepository
        self.place_repository = SQLAlchemyRepository(Place)
        self.review_repository = SQLAlchemyRepository(Review)
        self.amenity_repository = AmenityRepository()

    def create_place(self, place_data):
        owner_id = place_data.get('owner_id')
        if isinstance(owner_id, dict):
            owner_id = owner_id.get('id')
        if not owner_id:
            raise ValueError("owner_id is required")

        owner = self.user_repository.get(owner_id)
        if not owner:
            raise ValueError("Owner not found")

        try:
            price = float(place_data['price'])
            latitude = float(place_data['latitude'])
            longitude = float(place_data['longitude'])
        except (ValueError, KeyError):
            raise ValueError("Invalid numeric value for price, latitude or longitude")
        try:
            new_place = Place(
                id=None,
                owner=owner,
                title=place_data['title'],
                description=place_data.get('description'),
                price=price,
                latitude=latitude,
                longitude=longitude,
                created_at=None,
                updated_at=None
            )
        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid place data: {str(e)}")

        amenity_ids = place_data.get('amenities', [])
        for amenity_id in amenity_ids:
            amenity = self.amenity_repository.get(amenity_id)
            if amenity:
                new_place.add_amenity(amenity)

        review_ids = place_data.get('reviews', [])
        for review_id in review_ids:
            review = self.review_repository.get(review_id)
            if review:
                new_place.add_review(review)

        self.place_repository.add(new_place)
        return new_place


    def get_place(self, place_id):
        return self.place_repository.get(place_id)

    def get_all_places(self):
        return self.place_repository.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repository.get(place_id)
        if not place:
            return None

        if 'title' in place_data:
            place.title = place_data['title']
        if 'description' in place_data:
            place.description = place_data['description']
        if 'price' in place_data:
            try:
                place.price = float(place_data['price'])
            except ValueError:
                raise ValueError("Invalid price value")
        if 'latitude' in place_data:
            try:
                place.latitude = float(place_data['latitude'])
            except ValueError:
                raise ValueError("Invalid latitude value")
        if 'longitude' in place_data:
            try:
                place.longitude = float(place_data['longitude'])
            except ValueError:
                raise ValueError("Invalid longitude value")

        if 'owner_id' in place_data:
            owner = self.user_repository.get(place_data['owner_id'])
            if not owner:
                raise ValueError("Owner not found")
            place.owner = owner

        if 'amenities' in place_data:
            place.amenities.clear()
            for amenity_id in place_data['amenities']:
                amenity = self.amenity_repository.get(amenity_id)
                if amenity:
                    place.add_amenity(amenity)

        if 'reviews' in place_data:
            place.reviews.clear()
            for review_id in place_data['reviews']:
                review = self.review_repository.get(review_id)
                if review:
                    place.add_review(review)

        place.updated_at = datetime.now(timezone.utc)
        return place

    def delete_place(self, place_id):
       place = self.place_repository.get(place_id)
       return self.place_repository.delete(place)

    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.user_repository.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repository.get_user(user_id)

    def get_user_by_email(self, email):
        return self.user_repository.get_user_by_email(email)

    def put_user(self, user_id, new_data):
        user = self.get_user(user_id)
        if not user:
            return None
        user.update(new_data)
        return user


    def get_all_user(self):
        return self.user_repository.get_all_user()

    def create_amenity(self, amenity_data):
        return self.amenity_repository.create_amenity(amenity_data)

    def get_amenity(self, amenity_id):
        return self.amenity_repository.get_amenity(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repository.get_all_amenities()

    def update_amenity(self, amenity_id, amenity_data):
        return self.amenity_repository.update_amenity(amenity_id, amenity_data)

    def create_review(self, review_data):
        user = self.get_user(review_data["user_id"])
        place = self.get_place(review_data["place_id"])
        if not user or not place:
            raise ValueError("Invalid user_id or place_id")

        rating = review_data.get("rating")
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")

        review = Review(**review_data)
        self.review_repository.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repository.get(review_id)

    def get_all_reviews(self):
        return self.review_repository.get_all()

    def get_reviews_by_place(self, place_id):
        return self.review_repository.get(place_id)

    def update_review(self, review_id, review_data):
        review = self.get_review(review_id)
        if not review:
            return None
        self.review_repository.update(review_id, review_data)
        return review

    def get_review_by_user_and_place(self, user_id, place_id):
        all_reviews = self.review_repository.get_all()
        for review in all_reviews:
            if review.user_id == user_id and review.place_id == place_id:
                return review
        return None

    def delete_review(self, review_id):
       review = self.review_repository.get(review_id)
       return self.review_repository.delete(review)
