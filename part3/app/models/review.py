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

import uuid
from datetime import datetime, timezone

from app import db
from sqlalchemy import CheckConstraint


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


class Review(BaseModel):
    """Represents a review for a place made by a user."""

    __tablename__ = 'reviews'

    text = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5',
                        name='check_rating_range'),
    )
