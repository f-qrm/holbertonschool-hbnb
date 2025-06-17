#!/usr/bin/python3
import uuid
from datetime import datetime
from app.models.place import Place
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


class User(BaseModel):
    def __init__(self, id, created_at, updated_at, is_admin, first_name, last_name, email):
        super().__init__()
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_admin = is_admin
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.places = []
        self.reviews = []


    def new_place(self, place):
        self.places.append(place)


    def new_review(self, review):
        self.reviews.append(review)
