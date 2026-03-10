from django.urls import path
from . import views

# Add this in order to use it in templates later
app_name = "threads"

urlpatterns = [
    path("", views.index, name="index"),
    path("report/", views.report, name="report"),
    path("topics/", views.topics, name="topics"),
    path("other/", views.other, name="other"),
    # Click a link on the topics page, topics/<id> gets opened, pass the id to the views function to only
    # get the topic requested in the <id> field, html template fills out the id part (which topic you clicked on)
    path("topics/<int:topic_id>", views.topic, name="topic"),
    path("topics/<int:topic_id>/threads", views.threads, name="threads"),
    path("topics/<int:topic_id>/threads/<int:thread_id>", views.in_thread, name="in_thread"),
    path("topics/<int:topic_id>/threads/new_thread", views.new_thread, name="new_thread"),
    path("topics/<int:topic_id>/threads/<int:thread_id>/new_comment", views.new_comment, name="new_comment"),
    path("topics/<int:topic_id>/threads/<int:thread_id>/<int:comment_id>/new_reply", views.new_reply, name="new_reply")
]