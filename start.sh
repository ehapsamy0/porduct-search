#!/bin/bash

# Apply database migrations
python manage.py migrate

# Start server
# gunicorn --bind 0.0.0.0:8000 app.wsgi:application
python manage.py runserver 0.0.0.0:8000