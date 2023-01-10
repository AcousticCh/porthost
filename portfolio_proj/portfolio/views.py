from django.shortcuts import render

def index_view(request):
    return render(request, "index.html")

def project_list_view(request):

    context = None # ProjModel

    return render(request, "proj_list.html", context)

