from django.urls import path

from . import views

# URL configuration is defined
urlpatterns = [
    path("", views.index, name="index")
]
