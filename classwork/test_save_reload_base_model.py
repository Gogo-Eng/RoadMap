#!/usr/bin/python3

from models import storage
from models.base_model import BaseModel


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_Firt_Model"
my_model.my_number = 89
my_model.save()
print(my_model)


# gogo = BaseModel()
# gogo.save()
# print(gogo)
# print()
# print(gogo.__dict__)
# dictionary = gogo.to_dict()
# print(dictionary)
# print()
# for key in dictionary.keys():
#     print(f"\t{key}: ({type(dictionary[key])}) - {dictionary[key]}")

# progress = BaseModel(**dictionary)
# # print()
# print(progress.__dict__)