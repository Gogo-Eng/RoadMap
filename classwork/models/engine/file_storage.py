#!/usr/bin/python3

import json
import os
from datetime import datetime
from models.base_model import BaseModel

class FileStorage:
        
    __file_path = "file.json"
    __objects = {}
    
    def all(self, cls=None):
        if cls is None:
            return self.__objects
        else:
            cls_name = cls.__name__
            filtered_objects = {key: obj for key, obj in self.__objects.items() if key.startswith(cls_name)}
            return filtered_objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}" 
        self.__objects[key] = obj
    
    def classes(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review
                   }
        return classes
    
    def save(self):  
        with open(self.__file_path, "w") as file:
            json.dump({key: obj.to_dict() for key, obj in self.all().items()}, file)

    
    def reload(self):
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, "r") as file:
                    the_dict = json.load(file)
                    for key, value in the_dict.items():
                        cls_name, obj_id = key.split('.')
                        if cls_name in self.classes():
                            self.__objects[key] = self.classes()[cls_name](**value)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("error: json file is corrupted")
    
    def delete(self, obj=None):
        if obj == None:
            return
        key = f"{obj.__class__.__name__}.{obj.id}" 
        self.__objects[key]
        if key in self.__objects:
            del self.__objects[key]
            print("deleted")
        else:
            print("what's going on")
