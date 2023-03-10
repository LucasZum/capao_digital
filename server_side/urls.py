from django.urls import path

from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('register/create', views.create_user, name='create'),

]