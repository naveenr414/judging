from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import os
import time

# Create your views here.

def index(request):
	return HttpResponse("<h1> Hello World </h1>")

def problem(request):
	context = {}
	return render(request,'grading/problem.html', context)

def submit(request):
	fileName = request.POST['name']
	f = request.FILES['submission']
	with open("submissions/"+fileName+".py", 'wb') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

	start = time.time()
	os.system("cd submissions \n python3 "+fileName+".py")
	end = time.time()-start

	os.system("cd ../")

	if(end>=6):
		return HttpResponse('Your response took too long')
	else:
		realFile = open("answers/"+fileName+".out").read()
		theirs = open("submissions/"+fileName+".out").read()
		if(theirs == realFile):
			return HttpResponse("Nice job, you solved it")
		else:
			return HttpResponse("Wrong Answer")

	return HttpResponse(request.FILES['submission'].read())
