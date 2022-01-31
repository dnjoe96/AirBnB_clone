# AirBnB_clone

### Making a clone of the [airbnb.com](airbnb.com) application.

---

The aim of ths project is to create a clone of the Airbnb web application. Front-end clone as well as backend model clone.

---
#### Goals

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

---

### The console
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

For the backend interface of this application, you can interact with the application from the built python shell console.
##### *entry point* - ```console.py```

#### *run* - `./console.py` or `python3 console.py`

#### Example usage
```bash
donjoe@xxxxx:~/Desktop/alx/AirBnB_clone$ ./console.py 
(hbnb)
(hbnb)
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
(hbnb) help all
Prints all string representation of all instances based or not on
        the class name. Ex: $ all BaseModel or $ all
        
(hbnb)
(hbnb) help update
Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        Usage: update <class name> <id> <attribute name> "<attribute value>"

(hbnb) create User
e89ade3f-d450-4f14-977c-c8de28db9efd
(hbnb)
(hbnb) create City
bad15316-97e6-48a2-a17e-51f683e15c2e
(hbnb) create City
1bba447b-a778-4470-b820-b44f1eeae776
(hbnb) all City
["[City] (e90cdcdf-896e-44e6-a04b-01e3788ff823) {'id': 'e90cdcdf-896e-44e6-a04b-01e3788ff823', 'created_at': '2022-01-30T22:05:09.426735', 'updated_at': '2022-01-30T22:05:09.426751', '__class__': 'City', 'name': 'Bogota'}", "[City] (1e36788f-2f5a-4b1b-ab66-88f3a8fca3e1) {'id': '1e36788f-2f5a-4b1b-ab66-88f3a8fca3e1', 'created_at': '2022-01-30T22:05:19.429487', 'updated_at': '2022-01-30T22:05:19.429497', '__class__': 'City', 'name': 'Texas'}", "[City] (ffc40475-bc12-4cc1-bed8-d62219292625) {'id': 'ffc40475-bc12-4cc1-bed8-d62219292625', 'created_at': '2022-01-30T22:05:20.953561', 'updated_at': '2022-01-30T22:05:20.953571', '__class__': 'City'}", "[City] (bad15316-97e6-48a2-a17e-51f683e15c2e) {'id': 'bad15316-97e6-48a2-a17e-51f683e15c2e', 'created_at': '2022-01-31T05:11:18.242623', 'updated_at': '2022-01-31T05:11:18.242642', '__class__': 'City'}", "[City] (1bba447b-a778-4470-b820-b44f1eeae776) {'id': '1bba447b-a778-4470-b820-b44f1eeae776', 'created_at': '2022-01-31T05:11:25.777821', 'updated_at': '2022-01-31T05:11:25.777839', '__class__': 'City'}"]
(hbnb)
(hbnb) show City e90cdcdf-896e-44e6-a04b-01e3788ff823
[City] (e90cdcdf-896e-44e6-a04b-01e3788ff823) {'id': 'e90cdcdf-896e-44e6-a04b-01e3788ff823', 'created_at': '2022-01-30T22:05:09.426735', 'updated_at': '2022-01-30T22:05:09.426751', '__class__': 'City', 'name': 'Bogota'}
(hbnb)
(hbnb) destroy City e90cdcdf-896e-44e6-a04b-01e3788ff823
(hbnb)
(hbnb) show City e90cdcdf-896e-44e6-a04b-01e3788ff823
** no instance found **
(hbnb)
(hbnb) show City 1e36788f-2f5a-4b1b-ab66-88f3a8fca3e1
[City] (1e36788f-2f5a-4b1b-ab66-88f3a8fca3e1) {'id': '1e36788f-2f5a-4b1b-ab66-88f3a8fca3e1', 'created_at': '2022-01-30T22:05:19.429487', 'updated_at': '2022-01-30T22:05:19.429497', '__class__': 'City', 'name': 'Texas'}
(hbnb)
(hbnb) update City 1e36788f-2f5a-4b1b-ab66-88f3a8fca3e1 name Florida
(hbnb)
(hbnb) show City 1e36788f-2f5a-4b1b-ab66-88f3a8fca3e1
[City] (1e36788f-2f5a-4b1b-ab66-88f3a8fca3e1) {'id': '1e36788f-2f5a-4b1b-ab66-88f3a8fca3e1', 'created_at': '2022-01-30T22:05:19.429487', 'updated_at': '2022-01-30T22:05:19.429497', '__class__': 'City', 'name': 'Florida'}
(hbnb)
(hbnb)
(hbnb) quit
donjoe@xxxxx:~/Desktop/alx/AirBnB_clone$
```
---
### Web static
- learn HTML/CSS
- create the HTML of your application
- create template of each object

---

### MySQL storage
- replace the file storage by a Database storage
- map your models to a table in database by using an O.R.M.
---

### Web framework - templating
- create your first web server in Python
- make your static HTML file dynamic by using objects stored in a file or database
---

### RESTful API
- expose all your objects stored via a JSON web interface
- manipulate your objects via a RESTful API
---

### Web dynamic
- learn JQuery
- load objects from the client side by using your own RESTful API
---

### Authors
- [Rihana Ali Saeid](https://github.com/avocadoclouds)
- [Joseph Emmanuel](https://github.com/dnjoe96)