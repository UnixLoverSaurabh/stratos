from django.urls import path, include
from first_app import views

# Template Tagging
app_name = 'first_app'

urlpatterns = [
        path('', views.index, name='home'),
        path('emp/', views.showDatabaseRecords, name='employees'),
        path('contact/', views.subscribe, name='contact'),
        path('accounts/', include('django.contrib.auth.urls')),
]