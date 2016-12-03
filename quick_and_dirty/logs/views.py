# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import DailyLog

# Create your views here.
def daily_logs_list(self):
    logs = DailyLog.objects.all()
    output = '\n '.join([str(log) for log in logs])
    return  HttpResponse(output)

