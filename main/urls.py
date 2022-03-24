from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('successfully', views.successfully, name='successfully'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path("sign-up", views.registration, name='registration')
]
