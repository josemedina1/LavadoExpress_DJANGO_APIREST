import requests
from django.shortcuts import render

def home(request):

    url = "https://638cc70fd2fc4a058a5fbbdc.mockapi.io/s"

    servicios = requests.request("GET", url)
    servicios = servicios.json()

    dato = {
        'servicios': servicios
    }

    return render(request,'core/home.html',dato)


def carpinteria(request):
    return render(request,'core/carpinteria.html')


def error_404(request,exception):
    return render(request,'core/404.html')

