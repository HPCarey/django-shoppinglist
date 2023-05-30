This is a Shopping List app developed using django.  
You can visit the live site [here](https://django-shoppinglist.herokuapp.com/).

This project was developed on gitpod using VSCode.
Postgres is being used as the database and is being hosted on ElephantSQL for the deployed site.
Site is deployed to Heroku.
Gunicorn is being used as the wsgi HTTP server.

The setup commands for these were:
pip3 install 'django4'
pip3 install gunicorn
pip3 install dj_django_url==0.5.0 psycopg2

The superuser details are : username: admin  password:365

To run the server locally: python3 manage.py runserver
