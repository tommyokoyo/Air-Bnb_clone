#!/usr/bin/python3
"""
    BaseModel - serializes instances to a JSON file
                and deserializes JSON file to instances
"""
import json

class FileStorage:
    __file_path = 'file_storage.json'
    __objects = {}

    def all(self):
        """
            Returns all instances
            :return:
        """
        return self.__objects

    def new(self, obj):
        """
            Adds to the __objects dictionary with key
            <obj class name>.id
            :param obj:
            :return:
        """
        key = '{}.{}'.format(obj.__class__.__name__,obj.id)
        self.__objects[key] = obj

    def save(self):
        """
            Serializes instances to JSON file
            :return:
        """
        serialized_obj = {}
        for key, obj in self.__objects.items():
            serialized_obj[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_obj, file)

    def reload(self):
        """
            Deserializes instances from JSON file to __objects
            :return:
        """
        try:
            with open(self.__file_path, 'r') as file:
                loaded_obj = json.load(file)

            from models.base_model import Basemodel
            for key, obj in loaded_obj.items():
                class_name, object_id = key.split('.')
                cls = eval(class_name)
                obj = cls(**obj)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass












