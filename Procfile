web: gunicorn prometey_project.wsgi:application --preload --log-file - --bind 0.0.0.0:10000
release: python manage.py migrate --noinput

