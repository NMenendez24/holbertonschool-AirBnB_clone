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
        self.__objects['{}.{}'.format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        objs = self.__objects
        dump = {key: value.to_dict() for key, value in objs.items()}
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(dump, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as f:
                reloaded = json.load(f)
            for key, value in reloaded.items():
                FileStorage.__objects = reloaded
