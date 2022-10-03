👉Library 📚 Admin 👈

👉 Describtion 
This project is for Library Admin who can add , delete and update books of Library. anyone can access books but, admin only can operate the Library.
Project is built with Django Framework written in Python Language and Bootstrap css library for styling.


👉 Prerequisites 
 1. python version 3 or onword
 2. Django version 3 or onword

1. 🟢 Django==3.2.15
2. 🟢 Pillow==9.2.0
3. 🟢 mysqlclient==2.1.1


👉 Installations
  Create virtual envornment and activate it
 1. > virtualenv env
 2. >.\env\Scripts\activate.ps1 
 3. > pip install django
 
start django Project and create app
 1. django-admin startproject project-name
 2. python manage.py startapp app-name

creating and configuring mysql database with project.
  Open command line client (from mysql) and enter root password(login).
  1. > mysql> CREATE DATABASE db_name;
  2. > mysql> USE db_name

  In settings.py at DATABASE configuration
    
 1.   DATABASES = {
       'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'db_name',
            'USER' : 'user_name',
            'PASSWORD' : 'user_password' ,
            'HOST' : 'localhost',
            'PORT' : '3002',
        }
    }

  Installing mysqlclient 
  1. > pip install mysqlclient



👉 creating Model schema, url dispatching and Logic.
1. created Book Table with uuid as primary key and other fields like title , description etc.
2. register table in admin.py
  > admin.site.register(Book)
3. and migrate 
> python manage.py makemigrations
> python manage.py migrate







👉 Contact 
 @ iamlubie.shaikh@gmail.com /
 @ shaikhls2421@gmail.com





