from django.db import models
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, reverse
from datetime import datetime
from tinymce.models import HTMLField

from user.models import User
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length = 40)
    body = HTMLField()
    author = models.ForeignKey(User, related_name = "blogs", on_delete=models.CASCADE, blank = True, null=True)
    created_on = models.DateTimeField(default = datetime.now())

    category = models.ManyToManyField(Category, related_name = "blogs")

    last_updated = models.DateTimeField(blank = True, null = True)


    def __str__(self):
        return self.title + ", by: " + str(self.author)
    def  get_all_data(self):
        cats = ""
        try:
            cats = str(self.category)
        except:
            cats = ""
            for i in self.category:
                cats += str(i)
        print("cats for the blog: ", cats)
        return str(self.title) + str(self.author) + cats

