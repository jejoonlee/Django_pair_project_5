from django.shortcuts import render, redirect
from .models import Teacher, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
@login_required
def index(request):
  context = {
    'teachers' : Teacher.objects.all(),
  }
  return render(request, 'articles/index.html', context)

@login_required
def review(request, pk):
  teacher = Teacher.objects.get(pk=pk)

  comment_form = CommentForm()

  context = {
    'teacher':  teacher,
    'comment_form' : comment_form,
    'comments' : teacher.comment_set.all(),
  }
  return render(request, 'articles/review.html', context)

@login_required
def comment(request, pk):
  teacher = Teacher.objects.get(pk = pk)

  if request.method == "POST":
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.teacher = teacher
      comment.user = request.user
      comment.save()
  return redirect('articles:review', teacher.pk)

def comment_delete(request, pk, teacher_pk):
  comment = Comment.objects.get(pk=pk).delete()
  teacher = Teacher.objects.get(pk=teacher_pk)
  return redirect('articles:review', teacher.pk)

def like(request, teacher_pk, pk):
  comment = Comment.objects.get(pk=pk)

  if request.user not in comment.user_like.all():
    comment.user_like.add(request.user)
    is_like = True
  
  else:
    comment.user_like.remove(request.user)
    is_like = False

  data = {
    'isLike': is_like,
    'likeCount' : comment.user_like.all().count(),
  }
  return JsonResponse(data)