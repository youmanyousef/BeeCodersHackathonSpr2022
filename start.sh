#!/bin/bash
rm db.sqlite3
rm -rf app/migrations
python manage.py makemigrations app
python manage.py migrate
python manage.py createsuperuser
