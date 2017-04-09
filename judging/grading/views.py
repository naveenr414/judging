from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
	return HttpResponse("<h1> Hello World </h1>")

def problem(request):
	context = {}
	return render(request,'grading/problem.html', context)

def submit(request):
	return HttpResponse(request.POST['name'])
