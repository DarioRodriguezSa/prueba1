from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "inicio/home.html")

def actividades(request):
    return render(request, "actividad/actividades.html")