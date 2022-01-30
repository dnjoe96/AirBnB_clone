#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""

from . import storage
import uuid
from datetime import datetime


class BaseModel:
    """Class for base model of object"""

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance.
            Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute
        with the current datetime."""

        # if type(self.updated_at) != str:
        #     self.updated_at = datetime.now().isoformat()
        # else:
        #     self.updated_at = datetime.now()
        self.updated_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""
        if type(self.created_at) != str:
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        if type(self.updated_at) != str:
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        # print(type(created_at), type(updated_at))
        dic = self.__dict__
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = created_at
        dic['updated_at'] = updated_at
        return dic
