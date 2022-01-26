#!/usr/bin/python3
"""Module for FileStorage class."""


class FileStorage:

    def __init__(self):
        self.__file_path = 22
        self.__objects = 11

    def all(self):
        """Returns __objects dictionary."""
        pass

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        pass

    def save(self):
        """Serialzes __objects to JSON file."""
        pass

    def reload(self):
        """Deserializes JSON file into __objects."""
        pass
