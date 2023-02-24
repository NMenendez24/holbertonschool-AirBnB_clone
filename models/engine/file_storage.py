#!/usr/bin/python3
import json
import os


class FileStorage:
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        setattr(self.__objects, f"{obj.__class__.__name__}.{obj.id}", obj)
        """This doesn´t work we should make a loop to iterate through the keys"""

    def save(self):
        """serializes __objects to the JSON file"""
        objs_dump = {key: value.to_dict()
                     for key, value in self.__objects.items()}
        with open(self.__file_path, "w", encoding='utf-8') as fd:
            json.dump(objs_dump, fd)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as f:
                reloaded = json.load(f)
                for key, value in reloaded.items():
                    setattr(self.__objects, key, value)
