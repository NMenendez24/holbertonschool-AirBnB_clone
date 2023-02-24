#!/usr/bin/python3
import json
import os


class FileStorage():
    __objects = {}
    __file_path = "file.json"

    def all(self):
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        setattr(self.__objects, f"{obj.__name__}.{obj.id}", obj)

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        else:
            return
