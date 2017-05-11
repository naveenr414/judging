from django.db import models

class Submission(models.Model):
	submission_time = models.DateTimeField("Date Added")
	submission_location = models.CharField(max_length=200)
	user = models.CharField(max_length=200)

class Response(models.Model):
	submissionID = models.ForeignKey(Submission,on_delete=models.CASCADE)
	correct = models.BooleanField(default=False)


