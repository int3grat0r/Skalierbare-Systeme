# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime

# Create your models here.

class Todo(models.Model):
	name = models.CharField(max_length=80, help_text="todo eingeben")
	deadline = models.DateField(help_text="deadline eingeben")
	progress = models.IntegerField(help_text="progress eingeben")

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('model-detail-view', args=[str(self.id)])
