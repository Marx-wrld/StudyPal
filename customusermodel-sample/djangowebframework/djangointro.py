# What is Django?

##### Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It is free and open source.

## Django's MVC framework

##### URLs: While it is possible to process requests from every single URL via a single function, it is much more maintainable to write a separate view function to handle each resource. A URL mapper is used to redirect HTTP requests to the appropriate view based on the request URL. The URL mapper can also match particular patterns of strings or digits that appear in a URL and pass these to a view function as data.

##### View: A view is a request handler function, which receives HTTP requests and returns HTTP responses. Views access the data needed to satisfy requests via models, and delegate the formatting of the response to templates.

##### Models: Models are Python objects that define the structure of an application's data, and provide mechanisms to manage (add, modify, delete) and query records in the database.

##### Templates: A template is a text file defining the structure or layout of a file (such as an HTML page), with placeholders used to represent actual content. A view can dynamically create an HTML page using an HTML template, populating it with data from a model. A template can be used to define the structure of any type of file; it doesn't have to be HTML!

## urls.py

# urlpatterns defines a list of mappings between routes (specific URL patterns) and corresponding view functions. If an HTTP Request is received that has a URL matching a specified pattern, then the associated view function will be called and passed the request.

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('book/<int:id>/', views.book_detail, name='book_detail'),
#     path('catalog/', include('catalog.urls')),
#     re_path(r'^([0-9]+)/$', views.best),
# ]

## views.py

# Views are the heart of the web application, receiving HTTP requests from web clients and returning HTTP responses. In between, they marshal the other resources of the framework to access databases, render templates, etc.

##### code sample

# from django.shortcuts import render
# from .models import Team

# def index(request):
#     list_teams = Team.objects.filter(team_level__exact="U09")
#     context = {'youngest_teams': list_teams}
#     return render(request, '/best/index.html', context)


## models.py

# Django web applications manage and query data through Python objects referred to as models. Models define the structure of stored data, including the field types and possibly also their maximum size, default values, selection list options, help text for documentation, label text for forms, etc. The definition of the model is independent of the underlying database — you can choose one of several as part of your project settings. Once you've chosen what database you want to use, you don't need to talk to it directly at all — you just write your model structure and other code, and Django handles all the "dirty work" of communicating with the database for you.

##### code sample

# from django.db import models

# class Team(models.Model):
#     team_name = models.CharField(max_length=40)

#     TEAM_LEVELS = (
#         ('U09', 'Under 09s'),
#         ('U10', 'Under 10s'),
#         ('U11', 'Under 11s'),
#         # …
#         # list other team levels
#     )
#     team_level = models.CharField(max_length=3, choices=TEAM_LEVELS, default='U11')

## Rendering data using a html template

# Template systems allow you to specify the structure of an output document, using placeholders for data that will be filled in when a page is generated. Templates are often used to create HTML, but can also create other types of document. Django supports both its native templating system and another popular Python library called Jinja2 out of the box (it can also be made to support other systems if needed).

## code sample

# <!DOCTYPE html>
# <html lang="en">
# <head>
#   <meta charset="utf-8">
#   <title>Home page</title>
# </head>
# <body>
#   {% if youngest_teams %}
#     <ul>
#       {% for team in youngest_teams %}
#         <li>{{ team.team_name }}</li>
#       {% endfor %}
#     </ul>
#   {% else %}
#     <p>No teams are available.</p>
#   {% endif %}
# </body>
# </html>

#### Setting up the django development environment

# > cd Desktop
# > pip install python3
# > pip install django
# > django-admin --version
# > django-admin startproject test_app
# > cd test_app
# > pip install virtualenv
# > virtualenv venv
# > venv/Scripts/activate
# > python manage.py runserver