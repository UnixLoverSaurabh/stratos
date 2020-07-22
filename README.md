1. A migration allows us to move databases from one design to another, this is also reversible

2. $ python manage.py runserver

3. $ python manage.py startapp first_app

5. __init__.py
	Blank python script,
	python know that this directory can be treated as a package

6. admin.py
	We can register our models here which Django will then use them with Django's admin interface

7. apps.py
	Application specific configurations

8. models.py
	store the application's data models

9. tests.py
	store test functions to test our code

10. views.py
	functions that handle requests and return responses

11. Migrations folder
	stores database specific information as it relates to the models

12. {{}} used for simple text injection
	{%%} used for more complex injections and logic