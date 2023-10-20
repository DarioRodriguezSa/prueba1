from django.shortcuts import render, HttpResponse



def gastos(request):
    return render(request, "gasto/gastos.html")
