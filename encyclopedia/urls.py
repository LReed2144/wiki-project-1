from django.urls import path

from . import views

# URL configuration is defined
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry")

]
