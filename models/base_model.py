#!/usr/bin/python3
"""Define a class BaseModel and their methods"""

from uuid import uuid4
from datetime import datetime


class BaseModel():
    """BaseModel Class"""
    def __init__(self, *args, **kwargs):
        """Initialize"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key == "id":
                    setattr(self, key, str(uuid4))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """Str method"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """serializes __objects to the JSON file"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': type(self).__name__,
                         'created_at': self.created_at.isoformat(),
                         'updated_at': self.updated_at.isoformat()})
        return new_dict
