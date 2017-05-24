from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import os
import time
from users.models import User
from grading.models import Submission

# Create your views here.

def index(request):
	if('userId' in request.session):
		return HttpResponse(User.objects.get(pk=request.session['userId']))

	return HttpResponse("<h1> Hello World </h1>")

def problem(request):
	preceding = ""
	
	problemList = open(preceding+"answers/problemList.txt").read().split("\n")[:-1]

	context = {'problemList':problemList}

	return render(request,'grading/problem.html', context)

def fail(sub):
	sub.result = 0
	sub.save()

def win(sub):
	sub.result = 1
	sub.save()	

def submit(request):
	if(not ('userId' in request.session)):
		return HttpResponse("Not logged in")

	preceding = ""
	f = request.FILES['submission']
	
	submitTime = round(time.time())

	fileName = str(submitTime) + "_" + str(request.session['userId'])
	problemName = request.POST['name']

	with open(preceding+"submissions/"+fileName, 'wb') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
	
	#Time Location User Result
	sub = Submission(submissionTime = time.time(), submissionLocation = fileName, user = int(request.session['userId']))
	sub.save()	

	error = None
	start = time.time()
	attempt = os.system("cd submissions \n python3 "+fileName)
	if(attempt!=0):
		error="Compile"
		fail(sub)
		return HttpResponse("Your program failed to compile")
	end = time.time()-start

	if(end>=6):
		fail(sub)
		return HttpResponse('Your response took too long')
	else:
		realFile = open(preceding+"answers/"+problemName+".out").read()
		theirs = open(preceding+"submissions/"+problemName+".out").read()
	

		f = open(preceding+"submissions/"+problemName+".out","w")
		f.write(" ")
		f.close()

		if(theirs == realFile):
			win(sub)
			return HttpResponse("Nice job, you solved it")
		else:
			fail(sub)
			return HttpResponse("Wrong Answer")

	return HttpResponse(request.FILES['submission'].read())
