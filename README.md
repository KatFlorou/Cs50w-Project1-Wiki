# [Project1-Wiki-CS50w](https://cs50.harvard.edu/web/2020/projects/1/wiki/)

## Installation

```shell
cd ~/dev # Or wherever you develop
mkdir Project1-CS50w; cd Project1-CS50w
python3 -m venv venv # Create the virtual env
git clone git@github.com:KatFlorou/Project1-CS50w.git
```

Then install the packages

```shell
source venv/bin/activate
cd Project1-CS50w
pip install -Ur requirements.txt
```

Edit local settings to reflect your configuration

```shell
cp wiki/local_settings.py.example wiki/local_settings.py
wim wiki/local_settings.py
```

You can then run the server

```shell
python manage.py runserver # this defaults on 127.0.0.1:8000

```

## Python

This project requires python (minimum version 3.10) 

## Packages

This project requires multiple python packages to run, including Django.
Consult the file requirements.txt for such dependancies.

Don't forget to update the file whenever a package is installed, updated or removed

```python
pip freeze > requirements.txt # Write in a file all installed packages
pip install -Ur requirements.txt # Install all packages from a file
```
