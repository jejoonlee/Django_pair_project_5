from django.contrib import admin
from .models import Teacher, Comment

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
  pass

class CommentAdmin(admin.ModelAdmin):
  pass

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Comment, CommentAdmin)