web: gunicorn prometey_project.wsgi:application --preload --log-file - --bind 0.0.0.0:$PORT
release: python manage.py migrate --noinput

