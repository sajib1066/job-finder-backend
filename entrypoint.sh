#!/bin/bash

# Collect staticfiles
echo "Collect Staticfiles.............."
python manage.py collectstatic --noinput

echo "Wait for database................"
python manage.py wait_for_db

# Apply database migrations
echo "Apply database migrations........"
python manage.py migrate

# Start Server
echo "Starting Server.................."
python manage.py runserver 0.0.0.0:8000
