#!/usr/bin/python3
"""
Place module.

This module defines two classes: BaseModel and Place.
- BaseModel provides basic ID and timestamp functionality.
- Place represents a rental place, with validations on title, price,
  location, and relationships with amenities and reviews.
"""
from baseclass import BaseModel
from app.models.amenity import Amenity
from app.models.review import Review
from app import db


class Place(BaseModel):
    """
    Represents a place available for rental.

    Inherits from BaseModel and adds fields such as title, description,
    price, coordinates, and related amenities and reviews.

    Attributes:
        owner (User): The user who owns the place.
        title (str): Title of the place (max 100 characters).
        description (str): Optional description.
        price (float): Price per night (must be positive).
        latitude (float): Latitude coordinate (-90.0 to 90.0).
        longitude (float): Longitude coordinate (-180.0 to 180.0).
        amenities (list): List of associated Amenity objects.
        reviews (list): List of associated Review objects.
    """

    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(5000), nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
