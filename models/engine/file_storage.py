#!/usr/bin/python3
"""Module for FileStorage class."""


class FileStorage:

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns __objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        dkey = "{}.{}".format(type(obj).__name__, obj.id)
	FileStorage.__objects[dkey] = obj.to_dict()

    def save(self):
        """Serialzes __objects to JSON file."""
        serial_objs = json.dumps(FileStorage.__objects)

        if os.path.isfile(FileStorage.__file_path):
            if os.path.getsize(FileStorage.__file_path) == 0:
                obj_to_save = serial_objs

            else:
                obj_to_save = '\n' + serial_objs

        else:
		obj_to_save = serial_objs

        with open(FileStorage.__file_path, 'a') as f:
	    f.write(obj_to_save)

    def reload(self):
        """Deserializes JSON file into __objects."""
        pass
