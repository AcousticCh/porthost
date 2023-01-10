from django.urls import path
from . import views

name = "portfolio"
urlpatterns = [
    path("", views.index_view, name="index"),
]