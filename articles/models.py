from django.db import models
from django.conf import settings

# Create your models here.
class Teacher(models.Model):
  name = models.CharField(max_length=200)
  english_name = models.CharField(max_length=200)
  image = models.ImageField(upload_to='image/teacher_image', blank=True)

class Comment(models.Model):
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
  user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="comment_like")