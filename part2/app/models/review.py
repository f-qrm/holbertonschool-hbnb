#!/usr/bin/python3
import uuid
from datetime import datetime


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


class Review(BaseModel):
    def __init__(self, id, place, user, created_at, updated_at, rating, text):
        self.id = id
        self.place = place
        self.user = user
        self.created_at = created_at
        self.updated_at = updated_at
        self.rating = rating
        self.text = text
