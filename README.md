# [Cs50w-Project1-Wiki](https://cs50.harvard.edu/web/2020/projects/1/wiki/)

## Installation

```shell
cd ~/dev # Or wherever you develop
mkdir Cs50w-Project1-Wiki; cd Cs50w-Project1-Wiki
python3 -m venv venv # Create the virtual env
git clone git@github.com:KatFlorou/Cs50w-Project1-Wiki.git
```

Then install the packages

```shell
source venv/bin/activate
cd Cs50w-Project1-Wiki
pip install -Ur requirements.txt
```

Edit local settings to reflect your configuration

```shell
cp wiki/local_settings.py.example wiki/local_settings.py
```

You can then run the server

```shell
python manage.py runserver 

```

## Python

This project was created with Python 3.10.9 

## Packages

This project requires multiple python packages to run, including Django.
Consult the file requirements.txt for such dependancies.

Don't forget to update the file whenever a package is installed, updated or removed

```python
pip freeze > requirements.txt # Write in a file all installed packages
pip install -Ur requirements.txt # Install all packages from a file
```
