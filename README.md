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
    $ cd django django-1.5-template
    $ virtualenv --no-site-packages env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ cd django-1.5-template
    $ python manage.py syncdb
    $ python manage.py runserver
    
    open http://127.0.0.1:8000
    
