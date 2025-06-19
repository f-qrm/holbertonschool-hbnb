from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
import uuid
from datetime import datetime
from datetime import timezone


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def put_user(self, user_id, new_data):
        user = self.get_user(user_id)
        if not user:
            return None
        user.first_name = new_data.get('first_name', user.first_name)
        user.last_name = new_data.get('last_name', user.last_name)
        user.email = new_data.get('email', user.email)

        self.user_repo.update(user_id, new_data)
        return user

    def get_all_user(self):
        return self.user_repo.get_all()

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass
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
        self.amenity_repo.add(new_amenity)
        return new_amenity

    def get_amenity(self, amenity_id):
        amenity = self.amenity_repo.get(amenity_id)
        if amenity is None:
            return None
        return amenity

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if amenity is None:
            return None
        name = amenity_data.get('name')
        if not name:
            raise ValueError('Name invalid')
        amenity.name = name
        amenity.updated_at = datetime.now(timezone.utc)
        return amenity
