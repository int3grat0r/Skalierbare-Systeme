# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from catalog.models import Todo
from .forms import TodoForm

def index(request):
    """View function for home page of site."""

    todo_list = Todo.objects.all()

    context = {
        'todo_list': todo_list,
    }

    return render(request, 'index.html', context=context)


def page_new_task(request):
	return render(request, 'page_new_task.html')

"""
def page_edit_task(request):
	return render(request, 'page_edit_task.html')
"""
def page_impressum(request):
	return render(request, 'page_impressum.html')

"""
from .forms import TodoForm
def todo_new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.name = request.name
            todo.save()
            return redirect('page_new_task', id=todo.id)
    else:
        form = TodoForm()
    return render(request, 'page_new_task', {'form': form})

def todo_edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.name = request.name
            todo.save()
            return redirect('page_edit_task', id=todo.id)
    else:
        form = TodoForm(instance=post)
    return render(request, 'page_edit_task', {'form': form})
"""
def page_edit_task(request, id):
    item = Todo.objects.get(pk=id)
    if request.method == 'POST':
        form = EditItemForm(request.POST, instance=item)



