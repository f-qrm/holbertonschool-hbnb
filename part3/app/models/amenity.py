#!/usr/bin/python3
"""Base model and Amenity class module.

This module defines the BaseModel class for common attributes and behaviors,
and the Amenity class for storing information about place amenities.
"""

import uuid
from datetime import datetime, timezone

from app import db


class BaseModel(db.Model):
    """
    Base model class providing ID, created_at, and updated_at fields.

    Attributes:
        id (str): Unique identifier.
        created_at (datetime): Timestamp of instance creation.
        updated_at (datetime): Timestamp of last update.
    """
    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime,
                           default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime,
                           default=lambda: datetime.now(timezone.utc),
                           onupdate=lambda: datetime.now(timezone.utc))

    def save(self):
        """
        Updates the `updated_at` timestamp to the current time.
        """
        self.updated_at = datetime.now(timezone.utc)
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        """
        Updates instance attributes using a dictionary of key-value pairs.

        Args:
            data (dict): Dictionary of attributes to update.
        """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()


class Amenity(BaseModel):
    """Amenity class for describing a feature or service available
    in a place.

    Inherits from:
        BaseModel

    Attributes:
        name (str): Name of the amenity (e.g., "Wi-Fi", "Parking").
    """
    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False)

    """def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }"""
