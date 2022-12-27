from django.http import HttpResponse
from django.shortcuts import render


# HTTP request  <- HTTP response
def my_home(request):
    return render(request, 'recipes/home.html')
