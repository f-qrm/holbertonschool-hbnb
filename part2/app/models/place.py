#!/usr/bin/python3
import uuid
from datetime import datetime
from app.models.amenity import Amenity
from app.models.review import Review


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def save(self):
        self.updated_at = datetime.now()


    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()


class Place(BaseModel):


    def __init__(self, id, owner, created_at, updated_at, title, description, price, latitude, longitude):
        super().__init__()
        self.id = id
        self.owner = owner
        self.created_at = created_at
        self.updated_at = updated_at
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.amenitys = []
        self.reviews = []

    def add_amenity(self, amenity):
        self.amenitys.append(amenity)

    def add_review(self, review):
        self.reviews.append(review)
