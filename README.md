# Online Enrollment System (Django + Tailwind CSS)

## Run locally
    pip install -r requirements.txt
    python manage.py makemigrations students
    python manage.py migrate
    python manage.py createsuperuser      # this is your admin login
    python manage.py seed_students        # optional sample data
    python manage.py runserver

## Deploy on PythonAnywhere
1. Upload the zip (Files tab) and in a Bash console: `unzip enrollment_system.zip`
2. `mkvirtualenv venv --python=python3.10 && pip install -r enrollment_system/requirements.txt`
3. `cd enrollment_system && python manage.py makemigrations students && python manage.py migrate && python manage.py createsuperuser && python manage.py seed_students && python manage.py collectstatic`
4. Web tab -> Add a new web app -> Manual configuration (same Python version).
5. Source code + Working directory: `/home/<username>/enrollment_system`. Virtualenv: `/home/<username>/.virtualenvs/venv`
6. Edit the WSGI file so it contains:
       import os, sys
       path = '/home/<username>/enrollment_system'
       if path not in sys.path: sys.path.insert(0, path)
       os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
       from django.core.wsgi import get_wsgi_application
       application = get_wsgi_application()
7. Static files: URL `/static/` -> `/home/<username>/enrollment_system/staticfiles`
8. In `config/settings.py` add `<username>.pythonanywhere.com` to ALLOWED_HOSTS, set a new SECRET_KEY, then click Reload.
