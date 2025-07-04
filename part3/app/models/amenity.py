#!/usr/bin/python3
"""Base model and Amenity class module.

This module defines the BaseModel class for common attributes and behaviors,
and the Amenity class for storing information about place amenities.
"""
from sqlalchemy import Column, String
from baseclass import BaseModel
from app import db

class Amenity(BaseModel):
    """Amenity class for describing a feature or service available
    in a place.

    Inherits from:
        BaseModel

    Attributes:
        name (str): Name of the amenity (e.g., "Wi-Fi", "Parking").
    """

    __tablename__ = 'amenities'
    name = db.Column(db.String(128), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
