1. A migration allows us to move databases from one design to another, this is also reversible

2. $ django-admin startproject stratos

3. $ python manage.py runserver

4. $ python manage.py startapp first_app

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

13. Django comes equipped with SQLite

14. $ python manage.py migrate

15. Register the changes to our application
	$ python manage.py makemigrations first_app
	$ python manage.py migrate

16. $ python manage.py shell
	>>> from first_app.models import Topic
	>>> t = Topic(top_name="Social Network")
	>>> t.save()
	>>> print(Topic.objects.all())
	>>> quit()

17. $ python manage.py createsuperuser

18. Faker library to create script that will populate our model with some dummy data

19. Django - MTV (Models-Templates-Views)

20. Cross-Site-Request Forgery (CSRF) token, which secures the HTTP Post action that is initiated on the subsequent submission of a form.
	{% csrf_token %}

21. {{ form.as_p }} – Render Django Forms as paragraph

22. Relative URLs with templates
	Method-1:
		<a href="{% url 'thanku' %}">Thanks</a>
		name='thanku' is in the urls.py file

	Method-2:
		<a href="{% url 'first_app.views.thanku' %}">Thanks</a>

	Method-3:
		<a href="{% url 'first_app:thanku' %}">Thanks</a>
		this method requires that app_name variable to be created inside the urls.py file