from django.shortcuts import render
from .models import List


def home(request):
    lists = List.objects.all
    return render(request, 'todo_list/home.html', {'lists':lists})


def about(request):
    return render(request, 'todo_list/about.html', {})
