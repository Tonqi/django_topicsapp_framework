from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Topic, Thread, Comment
from .forms import ThreadForm, NewCommentForm, NewReplyForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    user = request.user
    context = {'user':user}
    return render(request, "threads/index.html", context)

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
        case 3:
            topic_message="I love anime."
        case 4:
            topic_message="Soccer, no it's football!"
        case _:
            topic_message="..."

    context = {'topic': topic, 'topic_message': topic_message}
    return render(request, "threads/topic.html", context)

def threads(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    # Parent -> get specific child with <model>_set
    topic_threads = topic.thread_set.order_by('-date_added')
    paginator = Paginator(topic_threads, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'topics':topic, 'topic_threads':page_obj,'page_obj': page_obj}
    return render(request, "threads/threads.html", context)

def in_thread(request, topic_id, thread_id):
    topic = Topic.objects.get(id=topic_id)
    thread = Thread.objects.get(id=thread_id)
    comments = thread.comment_set.order_by('-date_added')
    paginator = Paginator(comments, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'topics':topic, 'threads':thread, 'comments':page_obj, 'page_obj': page_obj}
    return render(request, "threads/in_thread.html", context)

@login_required
def new_thread(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if(topic.closed == False):
        if request.method != 'POST':
            form = ThreadForm()
        else:
            form = ThreadForm(data=request.POST)
            if form.is_valid():
                # Save the Thread but don't commit to DB yet
                new_thread_entry = form.save(commit=False)
                # Attach an owner first and a topic
                new_thread_entry.topic = topic
                new_thread_entry.owner = request.user
                # Send it to DB
                new_thread_entry.save()
                return redirect('threads:threads', topic_id=topic_id)
            
        context = {'topic':topic, 'form':form}
        return render(request, "threads/new_thread.html", context)
    else:
        raise Http404

@login_required
def new_comment(request, topic_id, thread_id):
    thread = Thread.objects.get(id=thread_id)
    if(thread.closed == False):
        form = NewCommentForm(data=request.POST)
        if form.is_valid():
            new_thread_comment = form.save(commit=False)
            new_thread_comment.owner = request.user
            new_thread_comment.thread = thread
            new_thread_comment.save() 
            return redirect('threads:in_thread', thread_id=thread_id, topic_id=topic_id)
    else:
        raise Http404
    if request.method == 'GET':
        raise Http404

@login_required
def new_reply(request, topic_id, thread_id, comment_id):
    thread = Thread.objects.get(id=thread_id)
    comment = Comment.objects.get(id=comment_id)
    if(thread.closed == False):
        form = NewReplyForm(data=request.POST)
        if form.is_valid():
            new_thread_reply = form.save(commit=False)
            new_thread_reply.owner = request.user
            new_thread_reply.comment = comment
            new_thread_reply.save()
            return redirect('threads:in_thread', thread_id=thread_id, topic_id=topic_id)
    else:
        raise Http404
    if request.method == 'GET':
        raise Http404