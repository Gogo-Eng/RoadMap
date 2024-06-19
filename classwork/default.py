
def default(self, arg):
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
    "update": self.do_update,
    "delete": self.do_delete,
    "count": self.do_count,
    "All": self.do_All
}

if incoming_method in method_dict:
    # print(type(command.split("(")[1][:-1]))
    # print(type(command.split("(")[0]))
    return method_dict[incoming_method](f"{incoming_class_name} {arg_string}")
else:   
    print(f"*** unknown syntax {arg}")
    eturn False