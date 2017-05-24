from django.db import models

class Submission(models.Model):
	submissionTime = models.IntegerField("Time Added")
	submissionLocation = models.CharField(max_length=200)
	user = models.CharField(max_length=200)

	#-1 is not graded, 0 = Failed, 1 = Pass
	result = models.IntegerField(default=-1)

class Response(models.Model):
	submissionID = models.ForeignKey(Submission,on_delete=models.CASCADE)
	correct = models.BooleanField(default=False)


