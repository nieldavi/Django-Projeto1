from django.urls import path

from . import views

# recipes:recipe

app_name = 'recipes'

urlpatterns = [
    path('', views.my_home, name="home"),  # home
    path('recipes/<int:id>/', views.recipe, name="recipe"),

]
