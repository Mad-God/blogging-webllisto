from django.db import models
from datetime import datetime
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.utils.text import slugify   
from user.models import User
from guardian.shortcuts import assign_perm
from tinymce.models import HTMLField


class PostQuerySet(models.QuerySet):
    def sorted(self):
        return self.order_by('-created_at')


    def category(self, cat):
        
        qsnew = cat.blogs.all()
        return qsnew




class PostManager(models.Manager):
    def sorted(self):
        return self.get_queryset().sorted()
        

    def get_queryset(self):
        return PostQuerySet(model=self.model, using=self._db)




class BlogCustomModel(models.Manager):
    pass

    def category(self, cat):
        return self.get_queryset().category(cat)


    def get_queryset(self):
        return PostQuerySet(model=self.model, using=self._db)



class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length = 40)
    body = HTMLField(max_length = 800, blank = True, null = True)
    author = models.ForeignKey(User, related_name = "blogs", on_delete=models.CASCADE, blank = True, null=True)
    created_on = models.DateTimeField(default = datetime.now())
    img = models.ImageField(upload_to = "blog/", blank = True, null = True)

    category = models.ManyToManyField(Category, related_name = "blogs", blank = True, null = True)

    last_updated = models.DateTimeField(auto_now = True, blank = True, null = True)

    objects = BlogCustomModel()

    deleted = models.BooleanField(default = False)

    published = models.BooleanField(default = False)

    slug = models.SlugField(unique=True)


    class Meta:
        permissions = [("can_change_blog", "can change this blog")]


    def __str__(self):
        return self.title + ", by: " + str(self.author)




def post_blog_created_signal(sender, instance, created, **kwargs):
    if created:
        instance.edited = None
        assign_perm(
            "blog.can_change_blog", 
            instance.author,
            instance
        )
        assign_perm(
            "blog.change_blog", 
            instance.author,
            instance
        )
        


 


def create_slug(instance, new_slug = None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Blog.objects.filter(slug = slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s"%(slug, qs.first().id)
        return create_slug(instance, new_slug = new_slug)
    return slug



def create_slug_category(instance, new_slug = None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Blog.objects.filter(slug = slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s"%(slug, qs.first().id)
        return create_slug(instance, new_slug = new_slug)
    return slug


def pre_blog_created_signal(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    



def pre_category_created_signal(sender, instance, **kwargs):
    
    if not instance.slug:
        instance.slug = create_slug_category(instance)
    





post_save.connect(post_blog_created_signal, sender = Blog)
pre_save.connect(pre_blog_created_signal, sender = Blog)
pre_save.connect(pre_category_created_signal, sender = Category)