#!/usr/bin/python3
"""This is our command interpeter for the AirBnB"""


import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class cmd"""
    prompt = '(hbnb)'
    new_classes = ['BaseModel', 'Amenity', 'City', 'Place',
    'Review', 'State', 'User']
    
    
    def do_quit(self, arg):
        """Quit to exit the program"""
    return True


    def do_EOF(self, arg):
        """EOF to exit the program"""
    return True


    def emptyline(self):
        """empty line"""
    pass


    def do_create(self, arg):
        """creates a new class"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.new_classes:
            print("** class doesn't exist **")
        else:
            inst = eval(line)()
            inst.save()
            print(inst.id)


    def do_show(self, line):
        """shows the string representation of an instance"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split() 
        if args[0] not in HBNBCommand.new_classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing**")
            return
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            names = f"{args[0]}.{args[1]}"
            print(storage.all()[names])


    def do_destroy(self, arg):
        """deletes an instance based on the classname"""
        
        args = arg.split()
        if arg == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.new_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            names = f"{args[0]}.{args[1]}"
            storage.all().pop(names)
            storage.save()


    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if line == "":
            obj = [str(obj) for key, obj in storage.all().items()]
            print(obj)
        else:
            if line not in HBNBCommand.new_classes:
                ("** class doesn't exist **")
        else:
        obj = [str(obj) for key, obj in storage.all().items()
                   if type(obj).__name__ == line]
        print(obj)


    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.new_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            name = f"{args[0]}.{args[1]}"
            obj = storage.all()[name]
            setattr(obj, args[2], args[3])
            obj.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
