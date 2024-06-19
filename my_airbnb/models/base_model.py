#!/usr/bin/env python3
import uuid
from datetime import datetime
datetime_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
           for  keys, value in kwargs.items():
                if keys == "created_at" or keys == "updated_at":
                    parsed_datetime = datetime.strptime(value, datetime_format)
                    self.__dict__[keys] = parsed_datetime
                elif keys == "__class__":
                    continue
                else:
                    self.__dict__[keys] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict