from django.shortcuts import render
from .models import ProjModel

def index_view(request):
    return render(request, "index.html")

def project_list_view(request):
    projects = ProjModel.objects.all()
    context = { "projects": projects }

    return render(request, "proj_list.html", context)

