from django.shortcuts import render
from .models import Teacher, Comment

# Create your views here.
def index(request):
  context = {
    'teachers' : Teacher.objects.all()
  }
  return render(request, 'articles/index.html', context)

def review(request, pk):
  teacher = Teacher.objects.get(pk=pk)

  context = {
    'teacher': teacher,
  }
  return render(request, 'articles/review.html', context)