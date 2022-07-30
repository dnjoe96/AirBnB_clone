#!/usr/bin/python3
""" Module for class FileStorage"""

import json
from os.path import exists
from models.base_model import BaseModel


class FileStorage:
    """ class that serialized instances to a json file and,
    deserializes a json file to instances. """

    # Private class attributes:

    # path to json file
    __file_path = "file.json"

    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    # Public instance methods:

    def all(self):
        """ Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        Sets the objects(obj) with key <obj class name>.id 
        in the __objects dictionary. 
        """
        # This wont work:
        # FileStorage.__objects[obj] = __class__.name__.id

        # we are trying to set our key inside
        # the __object dictionary in the  format ->
        # <object class name>. <obj.id>
        # So first we need to format the key then assign it a value obj
        # The 1st part <object class name> is the type of obj + the name
        # 2nd part is the just id

        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __onbjects dictionary to json file,
        path: __file_path
        """

        # In __objects there will be more
        # FileStorage.__file_path = json.dump(FileStorage.__objects)

        # Note: This won't work because we working with a file, not a variable
        # To make it work I need to use the file methods

        #----------------------------#
        # Steps to a dump a dictionery to json file
        # 1st: open file in w mode
        # 2nd: dump file or do this before opening
        # 3rd: write to a file
        # 4th: close file if didn't open 'with'

        with open(self.__file_path, "w") as json_file:

            # Note: the value variable here is an instance of class and
            #      we can't serialise an instance so, we need to generate
            #      a dictionary of that instance using the method .to_dict
            #      then we assign the dictionary back to the key, then
            #      we serialise the file.
            dict_storage = {}
            for key, value in self.__objects.items():
                dict_storage[key] = value.to_dict()
            json.dump(dict_storage, json_file)

    def reload(self):
        """
        deserializes the JSON file to __objects, if json file exits
        if no file, does nothing
        """

        # if exists(FileStorage.__file_path) == True:
        #     FileStorage.__objects = json.load(FileStorage.__file_path)
        # Note: This won't work because we working with a file, not a variable-
        # To make it work I need to use the file methods

        #--------------------------#
        # Steps to load json file to a dictionary
        # 1st: Open the file r mode
        # 2nd: load json in a dictionary
        # 3rd: close file

        try:
            if exists(self.__file_path):
                with open(self.__file_path, "r") as json_file:
                    # Note: now the value which a dictionary,
                    #  now is deserialised
                    obj_dict = json.load(json_file)
                    for key, value in obj_dict.items():
                        # explanation for this!!!
                        obj_dict = eval(value['__class__'])(**value)
                        self.__objects[key] = obj_dict

        except FileNotFoundError:
            return
