#!/usr/bin/python3
"""
    BaseModel - Defines common attributes
"""

import uuid
from datetime import datetime

class Basemodel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """
            String representation of Object
            :return:
        """
        return "[{}] {} {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            Updates the objects' updated_at
            :return:
        """
        self.updated_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

    def to_dict(self):
        """
            Converts the object to a dictionary
            :return:
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at
        obj_dict['updated_at'] = self.updated_at
        return obj_dict
