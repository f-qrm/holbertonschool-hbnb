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

    def __init__(self, id, owner, title, description, price, latitude,
                 longitude, created_at, updated_at):
        """
        Initializes a Place instance with full validation.

        Args:
            id (str): UUID of the place.
            owner (User): User instance representing the owner.
            title (str): Title of the place.
            description (str): Optional description.
            price (float): Price per night.
            latitude (float): Latitude coordinate.
            longitude (float): Longitude coordinate.
            created_at (datetime): Creation time.
            updated_at (datetime): Last update time.

        Raises:
            TypeError: If any argument is of the wrong type.
            ValueError: If constraints (length/range) are violated.
        """
        from app.models.user import User
        super().__init__(id=id, created_at=created_at, updated_at=updated_at)
        if not isinstance(owner, User):
            raise TypeError("owner must be a User instance")
        self.owner = owner

        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if len(title) > 100:
            raise ValueError("title must contain a maximum of 100"
                             "characters")
        self.title = title

        if description is not None and not isinstance(description, str):
            raise TypeError("description must be a string")
        self.description = description

        if not isinstance(price, float):
            raise TypeError("price must be a positive number")
        if price < 0:
            raise ValueError("price must be superior to 0")
        self.price = round(price, 2)

        if not isinstance(latitude, float):
            raise TypeError("latitude must be a number")
        if not -90 <= latitude <= 90:
            raise ValueError(
                "latitude must be within the range of -90.0 to 90.0")
        self.latitude = round(latitude, 1)

        if not isinstance(longitude, float):
            raise TypeError("longitude must be a number")
        if not -180 <= longitude <= 180:
            raise ValueError(
                "longitude must be within the range of -180.0 to 180.0")
        self.longitude = round(longitude, 1)

        self.amenities = []
        self.reviews = []

    def add_amenity(self, amenity):
        """
        Adds an Amenity object to the list of amenities.

        Args:
            amenity (Amenity): The amenity to add.
        """
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def add_review(self, review):
        """
        Adds a Review object to the list of reviews.

        Args:
            review (Review): The review to add.
        """
        self.reviews.append(review)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "owner_id": self.owner.id if self.owner else None,
            "owner": self.owner.to_dict() if self.owner else None,
            "amenities": [amenity.to_dict() for amenity in getattr(self, "amenities", [])],
            "reviews": [review.to_dict() for review in getattr(self, "reviews", [])]
        }
