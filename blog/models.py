from django.db import models
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, reverse
from datetime import datetime
from tinymce.models import HTMLField
from django.db.models import Count, F, Value, Q

from user.models import User




class PostQuerySet(models.QuerySet):
    # this method takes a queryset object and alters it how
    # we want.
    # so now we can use Post.objects.all().sorted()
    #  to get the queryset that we want
    def sorted(self):
        return self.order_by('-created_at')


    def category(self, cat):
        # print("asdaksjdhashdbjhabsd")
        # print(cat)
        # print(self.annotate(cats = F('category')).filter(cats__icontains = 'ML'))
        # breakpoint()
        qs = []
        model = self.model
        # qs = model.objects.none()
        # print(type(qs))
        print(self.__dict__)
        qs = []
        for i in self:
            print(i.category.all())
            if cat in i.category.all():
                # qs |= (i)
                qs.append(i.id)

        print("asdasdasdasd", qs)
        qsf = self.filter(id__in = qs)
        # breakpoint()
        return qsf
        # return self.annotate(cats = F('category')).filter(cats__icontains = cat.name)
# from blog.models import Blog, Category
# cat = Category.objects.last()
class PostManager(models.Manager):

    # now we can use Post.objects.sorted() to get the 
    # queryset we want
    def sorted(self):
        # get_queryset() returns all the instances of the
        #  current class

        # return self.get_queryset().order_by("-created_at")

        
        # but now we don't need this, since the QuerySet 
        # class has a sorted() method in itself
        
        # so we can redefine the class Queryset, so that it
        # has another method sorted, which will give us the 
        # data we want
        return self.get_queryset().sorted()
        

    # returns queryset object containing all the objects
    def get_queryset(self):

        # returning the custom queryset class object 
        # instead of the predefined queryset class
        return PostQuerySet(model=self.model, using=self._db)




class BlogCustomModel(models.Manager):
    pass

    def category(self, cat):
        # get_queryset() returns all the instances of the
        #  current class

        # return self.get_queryset().order_by("-created_at")

        
        # but now we don't need this, since the QuerySet 
        # class has a sorted() method in itself
        
        # so we can redefine the class Queryset, so that it
        # has another method sorted, which will give us the 
        # data we want
        
        return self.get_queryset().category(cat)


    def get_queryset(self):

        # returning the custom queryset class object 
        # instead of the predefined queryset class
        return PostQuerySet(model=self.model, using=self._db)



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

    last_updated = models.DateTimeField(auto_now = True, blank = True, null = True)

    objects = BlogCustomModel()


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

