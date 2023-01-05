from django.urls import path

from . import views

urlpatterns = [
    path('', views.my_home),  # home
    path('recipes/<int:id>/', views.recipe),

]
