#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        self.__dict__.update({'__class__': type(self).__name__,
                              'created_at': self.created_at.isoformat(),
                              'updated_at': self.updated_at.isoformat()})
        return self.__dict__
