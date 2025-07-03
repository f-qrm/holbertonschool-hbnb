#!/usr/bin/python3
"""
Module defining BaseModel, Review, and PlaceNotFoundError classes.

This module provides:
- A base model class (`BaseModel`) that handles unique IDs and timestamps.
- A review class (`Review`) that represents a review for a place by a user,
  with validation of attributes.
- A custom exception (`PlaceNotFoundError`) for cases where a place is not
found.

Classes:
    BaseModel: Base class with ID and timestamp attributes and basic
    save/update methods.
    Review: Model representing a user review of a place, including rating
    and text.

Imports:
    uuid: For generating unique string IDs.
    datetime: For managing timestamps.
    app.models.place.Place: The Place model representing a location.
    app.models.user.User: The User model representing a user.

Usage example:
    place = Place()
    user = User(first_name="Alice", last_name="Doe",
    email="alice@example.com")
    review = Review(id="1234", place=place, user=user, rating=5,
    text="Great place!")
"""

from baseclass import BaseModel



class Review(BaseModel):
    """Represents a review for a place made by a user."""

    def __init__(
            self, place_id, user_id, rating, text, id=None, created_at=None,
            updated_at=None
    ):
        """
        Initialize a new Review instance.

        Args:
            id (str): Unique identifier for the review.
            place (Place): The place being reviewed.
            user (User): The user who wrote the review.
            rating (int): The rating given in the review.
            text (str): The text content of the review.
            created_at (datetime, optional): Creation timestamp.
            updated_at (datetime, optional): Last update timestamp.

        Raises:
            TypeError: If any attribute is of incorrect type.
            TypeError: If the provided place is not a Place instance.
        """

        super().__init__(id=id, created_at=created_at, updated_at=updated_at)

        if not isinstance(place_id, str):
            raise TypeError("place must be a string")
        self.place_id = place_id

        if not isinstance(user_id, str):
            raise TypeError("User must be a string")
        self.user_id = user_id

        if not isinstance(rating, int):
            raise TypeError("rating must be an integer")
        self.rating = rating

        if not isinstance(text, str):
            raise TypeError("text must be a string")
        self.text = text
