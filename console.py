#!/usr/bin/env python3
"""Script for the project console"""
import cmd
import sys

from models import storage, all_models
# import readline
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

# histfile = os.path.join(os.path.expanduser("~"), ".python_history")


def initialize_class(class_name, dic=None):
    """This function is created for Dynamic initialization of model classes
    using the vars() function
    """
    if dic:
        return globals()[class_name](dic)
    else:
        return globals()[class_name]()


def args(arg):
    """
    Convert stream of characters, into a list of strings with space as
    delimiter
    """
    return arg.split()


def check_id(object_id):
    """concatenates the className and id, to check if the key exists in
    __object/file store
    """
    if object_id in list(storage.all().keys()):
        return True
    else:
        return False


def get_dict(object_key):
    """get the dictionary representation of an object with the object_key
    """
    return storage.all()[object_key]


class HBNBCommand(cmd.Cmd):
    """ Class to handle project commandline interpreter
    """

    prompt = '(hbnb) '
    file = None

    def __init__(self):
        """Initialize class to set parameter for non-intereactive
        operations
        """
        cmd.Cmd.__init__(self, stdin=sys.stdin)

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        """
        if len(arg) == 0:
            print("** class name missing **")
            return

        arg = args(arg)

        if arg[0] not in all_models:
            print("** class doesn't exist **")
            return

        obj = initialize_class(arg[0])
        storage.new(obj)
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234.
        """
        if len(arg) == 0:
            print("** class name missing **")
            return

        arg = args(arg)

        if arg[0] not in all_models:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return

        obj_id = arg[0] + '.' + arg[1]
        if check_id(obj_id):
            print(storage.all()[obj_id])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        if len(arg) == 0:
            print("** class name missing **")
            return

        arg = args(arg)

        if arg[0] not in all_models:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return

        obj_id = arg[0] + '.' + arg[1]
        if check_id(obj_id):
            storage._FileStorage__objects.pop(obj_id)
        # i think it may be a good idea to reload, but we'll see about that.
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name. Ex: $ all BaseModel or $ all
        """
        if len(arg) == 0:
            print("** class name missing **")
            return

        arg = args(arg)

        if arg[0] not in all_models:
            print("** class doesn't exist **")
            return

        all = []

        for key, value in storage.all().items():
            # key sample: BaseModel.b83e06b3-b296-42df-af3d-a880a26421f1
            if key.split('.')[0] == arg[0]:
                all.append(value)

        print(all)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if len(arg) == 0:
            print("** class name missing **")
            return

        arg = args(arg)

        if arg[0] not in all_models:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return

        obj_id = arg[0] + '.' + arg[1]
        if check_id(obj_id):
            dict_obj = get_dict(obj_id)
        else:
            print("** no instance found **")

        if len(arg) == 4:

            obj = initialize_class(arg[0], dict_obj)

            storage._FileStorage__objects[obj_id][arg[2]] = arg[3]
            obj.save()
        else:
            print("** Not enough paramters")

    def do_EOF(self, line):
        """EOF"""
        return True

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """ EXit the console and commit all changes"""
        storage.save()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
