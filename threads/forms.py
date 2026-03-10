from django import forms
from .models import Thread, Comment, Reply

# Create Forms in order to send something to the DB

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['thread_title','thread_description']
        labels ={'thread_title':'Enter a title for your Thread', 'thread_description' : 'Enter a Description for your Thread'}

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text':''}

class NewReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']
        labels = {'text':''}