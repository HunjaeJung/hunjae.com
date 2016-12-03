# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class DailyLog(models.Model):
    title = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at.strftime('%Y-%m-%d %H:%M')) + self.title.encode('utf-8')
