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

def page_edit_task(request):
	return render(request, 'page_edit_task.html')

def page_impressum(request):
	return render(request, 'page_impressum.html')

def delete(request, pk):
   elem = Todo.objects.get(pk = pk)
   print(elem.name)
   elem.delete()
   return HttpResponseRedirect('/catalog/')


