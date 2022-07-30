#!/usr/bin/python3
"""Module for FileStorage class."""

import json
import os


class FileStorage:
    """ The file storage handling class"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """Returns __objects dictionary."""
        # dic = {}
        # for key, value in FileStorage.__objects.items():
        #       dic[key] = value
        # return dic
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        dkey = "{}.{}".format(type(obj).__name__, obj.id)
        # FileStorage.__objects[dkey] = obj
        FileStorage.__objects[dkey] = obj.to_dict()

    def save(self):
        """Serializes __objects to JSON file."""
        # objs = {}
        # for key, value in FileStorage.__objects.items():
        #     objs[key] = value.to_dict()
        objs = FileStorage.__objects
        if len(FileStorage.__objects) != 0:
            serial_objs = json.dumps(objs)

            with open(FileStorage.__file_path, 'w') as f:
                f.write(serial_objs)

    def reload(self):
        """Deserializes JSON file into __objects."""
        FileStorage.__objects.clear()

        if not os.path.isfile(FileStorage.__file_path):
            return

        if os.path.getsize(FileStorage.__file_path) == 0:
            return

        with open(FileStorage.__file_path, "r") as f:
            FileStorage.__objects = json.loads(f.read())

        # for key, value in objs.items():
        # FileStorage.__objects[key] = \
        # globals()[value['__class__']](**value)
