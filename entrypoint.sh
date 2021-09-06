#!/usr/bin/env sh

sleep 10

python manage.py makemigrations
python manage.py migrate

python manage.py initadmin

gunicorn CRM.wsgi:application --bind 0.0.0.0:8000 --reload -w 4