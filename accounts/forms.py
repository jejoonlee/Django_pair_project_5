from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = get_user_model()
        fields = (
            'profile_name', 
            'group',
        )
        
        labels = {
            'profile_name': '변경할 닉네임', 
            'group': '학생 or 강사',
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = get_user_model()
        fields = (
            'username',
            'profile_name',
            'password1',
            'password2',
            # 'last_name',
            # 'first_name',
            # 'email',
            'gender',
            'group',
        )

        labels = {
            'username': '로그인 아이디',
            'profile_name': '사용할 닉네임',
            'password1': '비밀번호',
            'password2': '비밀번호 확인',
            # 'last_name': '성',
            # 'first_name': '이름',
            # 'email': '이메일',
            'gender': '성별',
            'group': '학생 or 강사',
        }

        widgets = {
            'username' : forms.TextInput(attrs={
                'class' : 'username',
            })

        }