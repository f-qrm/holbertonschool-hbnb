#!/usr/bin/python3
"""Base model and Amenity class module.

This module defines the BaseModel class for common attributes and behaviors,
and the Amenity class for storing information about place amenities.
"""
from baseclass import BaseModel


class Amenity(BaseModel):
    """Amenity class for describing a feature or service available
    in a place.

    Inherits from:
        BaseModel

    Attributes:
        name (str): Name of the amenity (e.g., "Wi-Fi", "Parking").
    """

    def __init__(self, name, id, created_at, updated_at):
        """Initializes an Amenity instance.

        Args:
            name (str): The name of the amenity. Must be a string of
            max 50 characters.
            id (str or None): Unique identifier. If None, a new UUID
            is generated.
            created_at (datetime or None): Creation timestamp.
            updated_at (datetime or None): Update timestamp.

        Raises:
            TypeError: If `name` is not a string.
            ValueError: If `name` exceeds 50 characters.
        """
        super().__init__(id=id, created_at=created_at, updated_at=updated_at)
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if len(name) > 50:
            raise ValueError("name must contain a maximum of 50 characters")
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
