#!/usr/bin/python3
"""Defines a class FileStorage and their methods"""
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage Class"""
    __objects = {}
    __file_path = "file.json"
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects['{}.{}'.format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        to_dump = {key: value.to_dict()
                   for key, value in self.__objects.items()}
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(to_dump, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as f:
                loaded = json.load(f)
            self.__objects = {}
            for key, value in loaded.items():
                key_class = key.split(".")[0]
                self.__objects[key] = self.classes[key_class](**value)
