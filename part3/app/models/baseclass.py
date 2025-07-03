from datetime import datetime
import uuid


class BaseModel:
    """Base model providing unique ID and timestamp management."""

    def __init__(self, id=None, created_at=None, updated_at=None):
        """
        Initialize a new BaseModel instance.

        Args:
            id (str, optional): Unique identifier. Generated if None.
            created_at (datetime, optional): Creation timestamp. Defaults
            to now.
            updated_at (datetime, optional): Last update timestamp. Defaults
            to now.
        """
        self.id = id if id else str(uuid.uuid4())
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()

    def save(self):
        """
        Update the `updated_at` timestamp to the current time.
        """
        self.updated_at = datetime.now()

    def update(self, data):
        """
        Update attributes of the instance based on a dictionary.

        Args:
            data (dict): Dictionary of attributes to update.
        """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
