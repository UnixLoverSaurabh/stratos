from django.urls import path
from first_app import views

# Template Tagging
app_name = 'first_app'

urlpatterns = [
        path('', views.index, name='home'),
        path('emp/', views.showDatabaseRecords, name='employees'),
        path('contact/', views.subscribe, name='contact'),
]