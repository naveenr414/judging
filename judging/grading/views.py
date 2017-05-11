from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import os
import time

# Create your views here.

def index(request):
	return HttpResponse("<h1> Hello World </h1>")

def problem(request):
	preceding = ""
	
	problemList = open(preceding+"answers/problemList.txt").read().split("\n")[:-1]

	context = {'problemList':problemList}

	return render(request,'grading/problem.html', context)

def submit(request):
	preceding = ""
	f = request.FILES['submission']
	
	fileName = f.name
	problemName = request.POST['name']

	with open(preceding+"submissions/"+fileName, 'wb') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

	error = None
	start = time.time()
	attempt = os.system("cd ../submissions \n python3 "+fileName)
	if(attempt!=0):
		error="Compile"
		return HttpResponse("Your program failed to compile")
	end = time.time()-start

	if(end>=6):
		return HttpResponse('Your response took too long')
	else:
		realFile = open(preceding+"answers/"+problemName+".out").read()
		theirs = open(preceding+"submissions/"+problemName+".out").read()
	

		f = open(preceding+"submissions/"+problemName+".out","w")
		f.write(" ")
		f.close()

		if(theirs == realFile):
			return HttpResponse("Nice job, you solved it")
		else:
			return HttpResponse("Wrong Answer")

	return HttpResponse(request.FILES['submission'].read())
