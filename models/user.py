#!/usr/bin/python3
"""class user that inherits form Base_model"""

from models.base_model import BaseModel


class User(BaseModel):
    """Subclass """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
