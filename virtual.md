# Creating a project

install virtual environment from pip
```bash
pip install virtualenv
```
Make directory and cd into it. Create a virtual environment in that directory
```bash
virtualenv venv
```
After running that command you'll find a folder called `venv`. This folder is the virtual environment and it hold all dependancies you'll need for this project.
To activate your environment run
```bash
source venv/bin.activate
```
Create new folder where your prioject will live. Inside the new directory create these files `requirement.txt, app.py`
```bash
touch requirement.txt, app.py
```
now you can install pip in that virtual environment. Just run pip install
```bash
pip install nose
```
To check dependancies installed in that environment by running
```bash
pip freeze
```
To add our dependancies to our requirements file
```bash
pip freeze > requirements.txt
```
To install our env from requirements file
```bash
pip install -r requirements.txt
```
To deactivate the environment just run
```bash
deactivate
```

Your folder structure should look like this
```bash
.
|
├── requirement.txt
├── app.py
├── src
|   ├── file_to_execute.py
|   └── __init__.py
└── test
    ├── test_file_to_execute.py
    └── __init__.py
```
