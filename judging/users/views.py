# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def login(request):
	return HttpResponse("Login")

def register(request):
	context = {}
	return render(request,'users/registration.html',context)

def registerComplete(request):
	return HttpResponse("Could not register successfully")