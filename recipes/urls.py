from django.urls import path

from recipes.views import my_contact, my_home, my_On

urlpatterns = [
    path('', my_home),  # home
    path('sobre/', my_On),
    path('contato/', my_contact),  # contato

]
