from django.shortcuts import render
from .models import Topic, Thread, Comment

# Create your views here.
def index(request):
    return render(request, "threads/index.html")

def report(request):
    return render(request, "threads/report.html")

def topics(request):
    topic = Topic.objects.order_by("date_added")
    # Get all topics and put them into a dictionairy - loop through them by accessing key 'topics'
    context = {'topics':topic}
    return render(request, "threads/topics.html", context)

def other(request):
    return render(request, "threads/other.html")

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    # Custom greet message upon entering a specific Topic
    topic_message=''
    match topic_id:
        case 1:
            topic_message="I fear technology, please no more!"
        case 2:
            topic_message="Don't talk rubbish about my favourite series!"
        case _:
            topic_message="..."

    context = {'topic': topic, 'topic_message': topic_message}
    return render(request, "threads/topic.html", context)

def threads(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    # Parent -> get specific child with <model>_set
    topic_threads = topic.thread_set.order_by('-date_added')
    context = {'topics':topic, 'topic_threads':topic_threads}
    return render(request, "threads/threads.html", context)

def in_thread(request, topic_id, thread_id):
    topic = Topic.objects.get(id=topic_id)
    thread = Thread.objects.get(id=thread_id)
    comments = thread.comment_set.order_by('-date_added')
    context = {'topics':topic, 'threads':thread, 'comments':comments}
    return render(request, "threads/in_thread.html", context)
