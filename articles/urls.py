from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:pk>/review/', views.review, name='review'),
  path('comment/<int:pk>/', views.comment, name='comment')
]