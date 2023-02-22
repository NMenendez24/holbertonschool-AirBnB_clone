#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

class BaseModel():
    def __init__(self, created_at, updated_at, id=None):
        self.id = str(uuid4())
        self.created_at = datetime.now
