#!/usr/bin/python3
"""Module for FileStorage autoinit."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

all_models = [
    'BaseModel',
    'User',
    'Amenity',
    'City',
    'Place',
    'Review',
    'State',
]
