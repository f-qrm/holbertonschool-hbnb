import uuid
from app import db
from app.models.amenity import Amenity
from datetime import datetime, timezone
from app.persistence.repository import SQLAlchemyRepository


class AmenityRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Amenity)
    def get_amenity(self, amenity_id):
        return self.get(amenity_id)
    def get_all_amenities(self):
        return self.model.query.all()
    def create_amenity(self, amenity_data):
        name = amenity_data.get('name')
        if not name or not isinstance(name, str):
            raise ValueError("Name is required and must be a string")
        new_amenity = Amenity(
            id=str(uuid.uuid4()),
            name=name,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        self.add(new_amenity)
        return new_amenity
    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get(amenity_id)
        if amenity is None:
            return None
        name = amenity_data.get('name')
        if not name or not isinstance(name, str):
            raise ValueError('Name is required and must be a string')
        amenity.name = name
        amenity.updated_at = datetime.now(timezone.utc)
        db.session.commit()
        return amenity
