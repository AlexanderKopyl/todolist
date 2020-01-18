from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            lists = List.objects.all
            messages.success(request, 'Item Has been added to list')
            return render(request, 'todo_list/home.html', {'lists': lists})
    else:
        lists = List.objects.all
        return render(request, 'todo_list/home.html', {'lists': lists})


def about(request):
    return render(request, 'todo_list/about.html', {})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'Item Has been deleted')
    return redirect('home')


def update(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = not item.completed
    item.save()
    messages.success(request, 'Item Has been Updated')
    return redirect('home')


def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, 'Item Has been Updated')
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'todo_list/edit.html', {'item': item})
