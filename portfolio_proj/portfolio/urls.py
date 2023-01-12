from django.urls import path
from . import views

app_name = "portfolio"
urlpatterns = [
    # path("resume/", views.resume_detail_view, name="resume"),
    path("projects/", views.project_list_view, name="projects"),
    path("", views.index_view, name="index"),
]