from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=264, unique=True)
    def __str__(self):
        return str(self.topic_name)

class Blog(models.Model):
    blog_topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    blog_title = models.CharField(max_length=100)
    blog_body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    blog_author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return str(self.blog_title)
