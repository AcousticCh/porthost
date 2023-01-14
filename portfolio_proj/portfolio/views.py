from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.apps import apps

def index_view(request):
    return render(request, "index.html")

def project_list_view(request):
    ProjModel = apps.get_model("portfolio", "ProjModel")
    LibModel = apps.get_model("portfolio", "LibModel")
    python_lib = get_object_or_404(LibModel, title="Python")
    python_projects = ProjModel.objects.filter(libraries__in=[python_lib])
    html_lib = get_object_or_404(LibModel, title="Html")
    html_projects = ProjModel.objects.filter(libraries__in=[html_lib])
    bash_lib = get_object_or_404(LibModel, title="Bash")
    bash_projects = ProjModel.objects.filter(libraries__in=[bash_lib])


    context = { "python_projects": python_projects, "html_projects": html_projects, "bash_projects": bash_projects }

    return render(request, "proj_list.html", context)

