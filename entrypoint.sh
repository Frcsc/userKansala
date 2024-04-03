#!/bin/bash

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start your Django application using Gunicorn
exec gunicorn white_paper.wsgi:application --bind 0.0.0.0:8000