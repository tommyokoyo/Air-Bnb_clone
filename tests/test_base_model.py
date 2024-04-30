#!/usr/bin/python3
from models.base_model import Basemodel

my_model = Basemodel()
my_model.name = "Sample_Model"
my_model.my_number = 69
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print('JSON of my model')
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print('---')
my_new_model = Basemodel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print('---')
print(my_model is my_new_model)