from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    teamName = models.CharField(max_length = 50)
    school = models.CharField(max_length = 50)

    #HASHED
    password = models.CharField(max_length=100)

    division = models.CharField(max_length=50)

    def __str__(self):
        return self.username
