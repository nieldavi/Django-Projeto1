from django.http import HttpResponse
from django.shortcuts import render


# HTTP request  <- HTTP response
def my_home(request):
    return render(request, 'recipes/pages/home.html')


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html')
