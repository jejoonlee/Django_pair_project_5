from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:pk>/review/', views.review, name='review'),
  path('comment/<int:pk>/', views.comment, name='comment'),
  path('comment_delete/<int:pk>/<int:teacher_pk>', views.comment_delete, name='comment_delete'),
  path('<int:pk>/like/<int:teacher_pk>/', views.like, name='like'),
]