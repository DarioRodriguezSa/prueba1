from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "inicio/home.html")

def eventos(request):
    return render(request, "evento/eventos.html")