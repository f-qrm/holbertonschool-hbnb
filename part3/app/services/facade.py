import uuid
from datetime import datetime, timezone

from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.models.user import User
from app.persistence.repository import SQLAlchemyRepository
from app.services.repositories.place_repository import PlaceRepository
from app.services.repositories.review_repository import ReviewRepository


class HBnBFacade:
    def __init__(self):
        self.user_repository = UserRepository()
        self.place_repository = PlaceRepository(
            self.user_repository,
            self.amenity_repository,
            self.review_repository
        )
        self.review_repository = ReviewRepository()
        self.amenity_repository = AmenityRepository()

    def create_place(self, place_data):
        return self.place_repository.create_place(place_data)

    def get_place(self, place_id):
        return self.place_repository.get_place(place_id)

    def get_all_places(self):
        return self.place_repository.get_all_places()

    def update_place(self, place_id, place_data):
        return self.place_repository.update_place(place_id, place_data)

    def delete_place(self, place_id):
        return self.place_repository.delete_place(place_id)

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repository.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repository.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repository.get_by_attribute('email', email)

    def put_user(self, user_id, new_data):
        user = self.get_user(user_id)
        if not user:
            return None
        user.update(new_data)
        return user

    def get_all_user(self):
        return self.user_repository.get_all()

    def create_amenity(self, amenity_data):
        name = amenity_data.get('name')
        if not name or not isinstance(name, str):
            raise ValueError("Name is required")
        new_amenity = Amenity(
            id=str(uuid.uuid4()),
            name=name,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
            )
        self.amenity_repository.add(new_amenity)
        return new_amenity

    def get_amenity(self, amenity_id):
        amenity = self.amenity_repository.get(amenity_id)
        if amenity is None:
            return None
        return amenity

    def get_all_amenities(self):
        return self.amenity_repository.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repository.get(amenity_id)
        if amenity is None:
            return None
        name = amenity_data.get('name')
        if not name:
            raise ValueError('Name invalid')
        amenity.name = name
        amenity.updated_at = datetime.now(timezone.utc)
        return amenity

    def create_review(self, review_data):
        return self.review_repository.create_review(review_data)

    def get_review(self, review_id):
        return self.review_repository.get_review(review_id)

    def get_all_reviews(self):
        return self.review_repository.get_all_reviews()

    def get_reviews_by_place(self, place_id):
        return self.review_repository.get_reviews_by_place(place_id)

    def update_review(self, review_id, review_data):
        return self.review_repository.update_review(review_id, review_data)

    def get_review_by_user_and_place(self, user_id, place_id):
        return self.review_repository.get_review_by_user_and_place(
            user_id, place_id)

    def delete_review(self, review_id):
        return self.review_repository.delete_review(review_id)
