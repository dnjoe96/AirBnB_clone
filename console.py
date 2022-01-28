import cmd, sys, os
# import readline
from models.base_model import BaseModel
from models import storage
# from models.engine.file_storage import FileStorage


# histfile = os.path.join(os.path.expanduser("~"), ".python_history")

def args(arg):
	"""Convert stream of characters, into a list of strings with space 
    as delimiter
	"""
	return arg.split()

def check_id(object_id):
	"""concatenates the className and id, to check if the key exists in 
    __object/file store
	"""
	# print(className + id)
	# print(list(storage.all().keys()))
	if object_id in list(storage.all().keys()):
		return True
	else:
		return False

# def get_dict(object_key):
# 	"""get the dictionary representation of an object with the object_key
# 	"""
# 	return storage.all()[object_key]

class HBNBCommand(cmd.Cmd):
	""" Class to handle project commandline interpreter
	"""
	
	# intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
	prompt = '(hbnb) '
	file = None

	# def do_help(self, arg):
	#   print("This is the help page")

	def do_create(self, arg):
		if len(arg) == 0:
			print("** class name missing **")
			return
		if arg not in ['BaseModel']:
			print("** class doesn't exist **")
			return
		obj = BaseModel()
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

		if arg[0] not in ['BaseModel']:
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
		"""Deletes an instance based on the class name and id (save the change 
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234
		"""
		if len(arg) == 0:
			print("** class name missing **")
			return
		
		arg = args(arg)

		if arg[0] not in ['BaseModel']:
			print("** class doesn't exist **")
			return
		if len(arg) < 2:
			print("** instance id missing **")
			return
		
		obj_id = arg[0] + '.' + arg[1]
		if check_id(obj_id):
			storage.del_obj(obj_id)
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

		if arg[0] not in ['BaseModel']:
			print("** class doesn't exist **")
			return
		
		all = []

		for key, value in storage.all().items():
			all.append(value)
		
		print(all)

		

	def do_update(self, arg):
		pass
	
	def do_EOF(self, line):
		return True

	def do_quit(self, arg):
		storage.save()
		exit()

if __name__ == '__main__':
  HBNBCommand().cmdloop()
