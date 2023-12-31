﻿# Content-Generator-AI
 **Creating a Flask Server**:
 
The flask object implements a WSGI application and acts as the central object. It is passed the name of the module or package of the application. Once it is created it will act as a central registry for the view functions, the URL rules, template configuration and much more.

The name of the package is used to resolve resources from inside the package or the folder the module is contained in depending on if the package parameter resolves to an actual python package (a folder with an __ init __.py file inside) or a standard module (just a .py file).

The below commands are used to run the  flask application

``` bash
cd Content-Generator-AI
# Create a virtual environment
python -m venv venv
```
``` bash
# Activate the virtual environment
venv\Scripts\activate
```
Install all dependencies
```python
pip install -r requirements.txt
```
``` python
# Run the Flask app
set FLASK_APP=app.py
flask run
```
**Creating a React Server**:

**#Installing Packages from package.json**

In a Node.js project, the package.json file lists the dependencies and other project-related information. To install packages listed in the package.json, follow these steps:

**1. Open Terminal:**
Navigate to the root directory of your project using the terminal or command prompt.

**2. Install Dependencies:**
Run the following command to install the packages listed in the package.json file:
```bash
npm install
```
This command will read the package.json file, download the listed packages, and store them in the node_modules directory.


**#Starting a React App**

Once you have your dependencies installed, you can start your React app. Here's how:

**1. Open Terminal:**
Navigate to the root directory of your React project using the terminal or command prompt.

**2. Start the Development Server:**
Run the following command to start the development server for your React app:
```bash
npm start
```

