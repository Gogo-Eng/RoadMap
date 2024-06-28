#!/usr/bin/python3
import models
import uuid
from datetime import datetime
from sqlalchemy import create_engine, text, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
class BaseModel:
    datetime_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        if kwargs:
            for keys, values in kwargs.items():
                if keys == "created_at" or keys == "updated_at":
                    dict_f = datetime.strptime(values, self.datetime_format)
                    self.__dict__[keys] = dict_f
                elif keys == "__class__":
                  continue
                else:
                    setattr(self, keys, values)
        else:    
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
    
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
