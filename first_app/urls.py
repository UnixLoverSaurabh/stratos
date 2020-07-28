from django.urls import path, include, re_path
from first_app import views

# Template Tagging
app_name = 'first_app'

urlpatterns = [
        path('', views.index, name='home'),
        path('signup/', views.signup, name='signup'),
        path('profile/', views.userProfile, name='userProfile'),
        path('emp/', views.showDatabaseRecords, name='employees'),
        path('contact/', views.subscribe, name='contact'),
        re_path('^', include('django.contrib.auth.urls')),
        re_path(r'^password_reset/$', auth_views.password_reset),
]