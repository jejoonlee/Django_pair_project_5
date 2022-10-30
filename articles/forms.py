from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = [
      'content',
    ]

    labels = {
      'content' : '',
    }

    widgets = {
      'content' : forms.Textarea(attrs={
        'class' : 'teachers-comment',
        'placeholder' : '댓글을 달아주세요',
        'rows' : 5,
      })
    }