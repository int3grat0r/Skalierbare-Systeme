# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from catalog.models import Todo

admin.site.register(Todo)
