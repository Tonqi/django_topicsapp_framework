from django import forms
from .models import Thread, Comment, Reply

# Create Forms in order to send something to the DB

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['thread_title','thread_description']
        labels = {
            'thread_title': '',
            'thread_description': '' 
        }
        widgets = {
            'thread_title': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter title'}),
            'thread_description': forms.Textarea(attrs={'class': 'form-control','rows': 3, 'placeholder': "Description"}),
        }



class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': '' 
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control','rows': 3}),
        }

class NewReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']
        labels = {
            'text': '' 
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control','rows': 3}),
        }