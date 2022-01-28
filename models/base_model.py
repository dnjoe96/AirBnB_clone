#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""

from models import storage
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

        print(len(kwargs))
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            self.id = kwargs['id']
            self.created_at = datetime.strptime(kwargs
                            ['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            self.update_at = datetime.strptime(kwargs
                    ['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

    
    def __str__(self):
        """Returns a string representation of the instance"""

        return "[{}] ({}) {}".format(__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute
        with the current datetime."""

        self.update_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""

        created_at = self.created_at.isoformat()
        updated_at = self.updated_at.isoformat()

        dic = self.__dict__
        dic['__class__'] = __class__.__name__
        dic['created_at'] = created_at
        dic['updated_at'] = updated_at
        return dic
