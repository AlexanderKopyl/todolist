from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('update/<list_id>', views.update, name="update"),
    path('edit/<list_id>', views.edit, name="edit"),
]