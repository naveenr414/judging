from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    teamName = models.CharField(max_length = 50)
    school = models.CharField(max_length = 50)

    division = models.CharField(max_length=50)
