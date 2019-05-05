# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime


class Todo(models.Model):
	name = models.CharField(max_length=80)
	deadline = models.DateField()
	progress = models.IntegerField()

	def __str__(self):
		return self.name
