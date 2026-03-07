from django.contrib import admin
from .models import Topic, Thread, Comment, Reply

# Register your models here.
admin.site.register(Topic)
admin.site.register(Thread)
admin.site.register(Comment)
admin.site.register(Reply)