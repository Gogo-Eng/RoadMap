#!/usr/bin/python3

import cmd
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import re

class GogoConsole(cmd.Cmd):

    prompt = "(frontman) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    
    def do_quit(self, arg):
        """
        quit command is used to exit the console
        """
        print("** Console Terminated **")
        return True

    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        print("*** End of file")
        return True
    
    def default(self, arg):
        try:
            arg_list = arg.split(".")
        
            incoming_class_name = arg_list[0]
            command = arg_list[1]
        
        
            if "(" not in command or ")" not in command:
                 print(f"*** unknown syntax")
                 return
            # handles case like User.g ie a random command that doesn't have () eg User.df()

            incoming_method = command.split("(")[0]
            arg_string = command.split("(")[1][:-1]

            method_dict = {
                "all": self.do_all,
                "create": self.do_create,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "updates": self.do_update,
                "delete": self.do_delete,
                "count": self.do_count,
                "All": self.do_All
            }

            
            if incoming_method == "update":
                id_str, line = arg_string.split(", ", 1)
                id = id_str.strip("\"")
                if line.startswith("{"):
                    json_cmd = line.replace("\'", "\"")
                    dict_cmd = json.loads(json_cmd)
                
                    objects = storage.all()
                    key = f"{incoming_class_name}.{id}"
                    if key not in objects:
                        print("** no instance found **")
                    obj = objects[key]
                    for k, v in dict_cmd.items():
                        setattr(obj, k, v)
                    obj.save()
                else:
                    return method_dict["updates"](f"{incoming_class_name} {arg_string}")

            elif incoming_method in method_dict:
                # print(type(command.split("(")[1][:-1]))
                # print(type(command.split("(")[0]))
                return method_dict[incoming_method](f"{incoming_class_name} {arg_string}")
            else:   
                # print(f"*** unknown syntax {arg}")
                # return False
                super().default(arg)
        except Exception:
            print(f"{arg}: command not found")

    def do_create(self, arg):
        command = shlex.split(arg)

    
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[command[0]]()
           # new_instance.save()
           # object = storage.all()
           # key = f"{command[0]}.{new_instance.id}"
           # obj = object[key]
            
            for param in command[1:]:
                key_value = param.split("=", 1)
                k, v = key_value
                k = k.replace('_', ' ')
                v = self.parse_value(v)
                setattr(new_instance, k, v)
            print(new_instance.id)
            new_instance.save()
            # obj.save()


    def parse_value(self, value):
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1].replace('_', ' ').replace('\\"', '"')
            return value
    
        else:
            try:
                if '.' in value:
                    return float(value)
                return int(value)
            except ValueError:
                return value
            
    def do_show(self, arg):
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = f"{command[0]}.{command[1]}"
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
    
    def do_destroy(self, arg):
        #return self.do_update(arg)
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = f"{command[0]}.{command[1]}"
            if key in objects:
                del objects[key]
            else:
                print("** no instance found **")
    
    def do_all(self, arg):
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            for key, value in objects.items():
                class_name, class_id = key.split('.')
                if class_name == command[0]:
                    print([str(value)])

    def do_update(self, arg):
        command = shlex.split(arg)

        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif len(command) == 2:
            print("** attribute name missing **")
        elif len(command) == 3:
            print("** value missing **")
        else:
            objects = storage.all()
            key = f"{command[0]}.{command[1]}"
            obj = objects[key]
            
            if key in objects:
               obj.__dict__[command[2]] = command[3]
               obj.save()
                #setattr(obj, command[2], command[3])
            else:
                print("** no instance found **")

    def do_delete(self, arg):
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif len(command) == 2:
            print("** attribute name missing **")
        else:
            objects = storage.all()
            key = f"{command[0]}.{command[1]}"
            obj = objects[key]
            
            if key in objects:
               del obj.__dict__[command[2]]
            else:
                print("** no instance found **")
    
    def do_count(self, arg):
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.classes:
            print("** class doesn't exist **")
        
        else:
            objects = storage.all()
            for key, value in objects.items():
                class_name, class_id = key.split('.')
                if class_name == command[0]:
                    class_instance_key = [keys for keys in objects if keys.startswith(class_name)]
                else:
                    class_instance_key = []
            print(len(class_instance_key))
            


    def do_All(self, arg):
        if arg:
            print(f"*** unknown syntax: All command does not take any arguments")  
            return  
        objects = storage.all()
        for key, value in objects.items():
            print(value)
        

        

if __name__ == '__main__':
    GogoConsole().cmdloop()
    