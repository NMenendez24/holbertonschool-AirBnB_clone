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
        objs = {key: value.to_dict()
                for key, value in self.__objects.items()}
        with open(self.__file_path, "w", encoding='utf-8') as fd:
            json.dump(objs, fd)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as f:
                reloaded = json.load(f)
                for key, value in reloaded.items():
                    setattr(self.__objects, key, value)
