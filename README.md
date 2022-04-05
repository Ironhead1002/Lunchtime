#CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Recommended modules
 * Installation
 * Configuration
 
#INTRODUCTION
------------
    Our system provides solution to make lunch service, easy and readily accesible for all the simform employees by lowering the waiting time and showing the approximate number of people having lunch in real-time.

#REQUIREMENTS
------------
    This module requires following modules:
    *[lunchtime](This is the project)
    *[menu] (this is app)
    *[canteenInfo] (this is app)
    *[reviews] (this is app)
    *[userdetail] (this is app)
    

#INSTALLATION
------------
    install the following versions of the below mentioned libraries
    *psycopg2-binary == 2.9.3
    *Django == 4.0.3
    *django-rest-passwordreset
    *djangorestframework == 3.13.1
    *Pillow == 9.1.0
    *django-environ==
    

#CONFIGURATION
-------------
    *Configure the below mentioned changes in settings.py file

    -INSTALLED_APPS:
        'django.contrib.admin',
    	'django.contrib.auth',
    	'django.contrib.contenttypes',
    	'django.contrib.sessions',
    	'django.contrib.messages',
    	'django.contrib.staticfiles',
    	'menu',
    	'reviews',
    	'userdetail',
    	'canteenInfo',
    	'rest_framework',
    	'django_rest_passwordreset',

