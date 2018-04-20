#!/bin/bash
python manage.py collectstatic --noinput
python manage.py makemigrations account
python manage.py makemigrations
python manage.py initializer # Please comment out if you use your own django files
python manage.py migrate
python manage.py loaddata initial_data.json
