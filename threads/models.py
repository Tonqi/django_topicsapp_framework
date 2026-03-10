from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    def __str__(self):
        return self.topic_name

class Thread(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    thread_title = models.CharField(max_length=100)
    thread_description = models.TextField()
    # thread_creator - TODO: User that created the thread
    date_added = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        if(len(self.thread_title)>30):
            return f"{self.thread_title[:30]}..."
        return self.thread_title

class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        if(len(self.text)>10):
            return f"{self.text[:10]}..."
        return self.text

# Reply to either the OP or comments, keep it simple in the beginning, don't nest replies yet.
class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural = "Replies"
    def __str__(self):
        if(len(self.text)>10):
            return f"{self.text[:10]}..."
        return self.text

