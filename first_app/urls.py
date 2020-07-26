from django.urls import path, include
from first_app import views

# Template Tagging
app_name = 'first_app'

urlpatterns = [
        path('', views.index, name='home'),
        path('signup/', views.signup, name='signup'),
        path('emp/', views.showDatabaseRecords, name='employees'),
        path('contact/', views.subscribe, name='contact'),
        path('accounts/', include('django.contrib.auth.urls')),
]