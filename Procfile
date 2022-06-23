release: python manage.py migrate --no-input
web gunicorn blog_post.wsgi:application --log-file -