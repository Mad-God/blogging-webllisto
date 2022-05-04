from django.db import models
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, reverse
from datetime import datetime
from tinymce.models import HTMLField

from user.models import User

class Blog(models.Model):
    title = models.CharField(max_length = 40)
    body = HTMLField()
    author = models.ForeignKey(User, related_name = "blogs", on_delete=models.CASCADE)
    created_on = models.DateTimeField(default = datetime.now())

    last_updated = models.DateTimeField(blank = True, null = True)


    def __str__(self):
        return self.title + ", by: " + str(self.author)


