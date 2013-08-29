django-1.5-template
===================

1. starter project
2. custom registration
3. cerulean boostrap template - [http://bootswatch.com/cerulean/](http://bootswatch.com/cerulean/)


I use this template for most starter projects.


How to quickly try this on your computer
------------------------

If you have git and Python installed, you can run the following commands to setup this project on your computer and run it to see how it works.

    $ git clone https://github.com/mjhea0/django-1.5-template.git
    $ cd django-1.5-template
    $ virtualenv --no-site-packages env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ cd django-1.5-template
    $ python manage.py syncdb
    $ python manage.py runserver
    
open http://127.0.0.1:8000

Push to Heroku
-------

1. Install the django-toolbelt:
        
        $ pip install django-toolbelt

2. Add the Procfile:

        $ touch Procfile    

3. Insert the following code into the Procfile:

        web: gunicorndjango-15-template.wsgi
    
4. Test locally:

    $ foreman start
    
5. Udate the requirements:

    $ pip freeze > requirements.txt

6. Append the following code to settings.py

        # Parse database configuration from $DATABASE_URL
        import dj_database_url
        DATABASES['default'] =  dj_database_url.config()
        
        # Honor the 'X-Forwarded-Proto' header for request.is_secure()
        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
        
        # Allow all host headers
        ALLOWED_HOSTS = ['*']
        
7. Update wsgi.py:

        import os
        
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-15-template.settings")
        
        from django.core.wsgi import get_wsgi_application
        from dj_static import Cling
        
        application = Cling(get_wsgi_application())
        
8. Initiate a local Git repo:

        $ git init
        $ git add .
        $ git commit -m "first commit"
        
9. PUSH to Heroku

        $ heroku create
        $ git push heroku master
        
10. Add postgres:

        $ heroku addons:add heroku-postgresql:dev
        $ heroku pg:promote [NAME OF DATABASE]
        
11. Sync the DB:

        $ heroku run python manage.py syncdb
        
12. Test:

        $ heroku open

