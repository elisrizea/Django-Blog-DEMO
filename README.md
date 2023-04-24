
# **Simple Django Blog DEMO**
    Django demo showcasing forms and Restful API. Features include:
    View all posts on homepage or using api (read only for unregistered users)
    User registration and login forms
    Logged in users can post new forms using built-in form or API
    RESTful API available at <website name>/api/
    Simple and easy-to-understand code.

# **Description:**
    This is a Django web app allowing registered users to share their thoughts online. 
    The app has a dashboard displaying latest posts ordered by date. Users can post their   
    thoughts from their profile, and all posted thoughts are stored in a MySql database. 
    The app also includes Restful APIs for getting and storing posts, and a contact form 
    for users to send messages. The app has tests for all views in the main_app and sendmail apps.


# **Require:**
    Require venv, django and django rest framework
    *Django: https://www.djangoproject.com/
    *Django Rest Framework: https://www.django-rest-framework.org/

# **Installation:**
    pip install virtualenv
    virtualenv env
    source env/bin/activate
    pip install django
    pip install djangorestframework

    
# **Running:**
    python manage.py migrate
    python manage.py runserver


# **Credits:**
    Alin Rizea
    https://www.linkedin.com/in/alin-rizea-b10368104/