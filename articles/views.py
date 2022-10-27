from django.shortcuts import render, redirect
from .models import Teacher, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

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
    'teacher': teacher,
    'comment_form' : comment_form,
    'comments' : Comment.objects.all(),
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
