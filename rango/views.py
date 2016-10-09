from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest


def index(request):
    context_dict = {'boldmessage': 'Crunchy, Creamy , Cookie, Candy, Cupcake'}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html', context=None)
    # return HttpResponse("Rango says here is the about page <a href='/rango'> back  </a>")
