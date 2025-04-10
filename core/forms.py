from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Answer


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title.strip()) < 10:
            raise forms.ValidationError("Title must be at least 10 characters long.")
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if not content.strip():
            raise forms.ValidationError("Content cannot be empty.")
        return content


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data['content']
        if not content.strip():
            raise forms.ValidationError("Answer cannot be empty or just spaces.")
        return content
