from django import forms
from .models import Thread, Comment, Reply

# Create Forms in order to send something to the DB

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['thread_title','thread_description']
        widgets = {
            'thread_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'thread_description': forms.Textarea(attrs={'class': 'form-control','rows': 3}),
        }

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control','rows': 3}),
        }

class NewReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control','rows': 3}),
        }