#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime


class BaseModel():
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__.update({'__class__': type(self).__name__,
                              'created_at': self.created_at,
                              'updated_at': self.updated_at.isoformat()})
        return self.__dict__
