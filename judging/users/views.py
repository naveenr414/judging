# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from users.models import User
import hashlib

# Create your views here.
def login(request):
	context = {}
	return render(request,'users/login.html',context)

def loginConfirm(request):
	username=request.POST['username']
	password=hashlib.md5(request.POST['password'].encode()).hexdigest()
	
	if(User.objects.filter(username=username).count()):
		attempt = User.objects.filter(username=username)[0]
		if(attempt.password == password):
			request.session['userId'] = attempt.id
			return HttpResponse("Works")
	
	return HttpResponse("Doesn't Work")	

def logout(request):
	if('userId' in request.session):
		del request.session['userId']
	
	return HttpResponse("Not logged in anymore")

def register(request):
	context = {}
	return render(request,'users/registration.html',context)

def registerComplete(request):
	username = request.POST['username']
	hashedPassword = hashlib.md5(request.POST['password'].encode()).hexdigest()
	school = "RMHS"
	teamName="Pentacontagons"
	division="Middle School"

	if(User.objects.filter(username=username).count()):
		return HttpResponse("Choose a new username")
	else:	
		u = User(username=username,teamName=teamName,division=division,password=hashedPassword,school=school)
		u.save()

		return HttpResponse("It worked")
