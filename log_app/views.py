from django.shortcuts import render, redirect
from . import models
from . import forms
from django.http import Http404
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'log_app/index.html')


@login_required
def topics(request):
    topics_context = models.Topic.objects.filter(owner=request.user)
    context = {'topics': topics_context}
    return render(request, 'log_app/topics.html', context=context)


@login_required
def topic(request, topic_id):
    topic_context = models.Topic.objects.get(id=topic_id)
    if topic_context.owner != request.user:
        raise Http404
    entries = topic_context.entry_set.order_by('-create_at')
    context = {'topic': topic_context, 'entries': entries}
    return render(request, 'log_app/topic.html', context=context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form = forms.TopicForm()
    else:
        form = forms.TopicForm(data=request.POST)
        if form.is_valid():
            add_owner = form.save(commit=False)
            add_owner.owner = request.user
            add_owner.save()
            return redirect('log_app:topics')

    context = {'form': form}
    return render(request, 'log_app/new_topic.html', context=context)


@login_required
def new_entry(request, topic_id):
    topic_context = models.Topic.objects.get(id=topic_id)
    if topic_context.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = forms.EntryForm
    else:
        form = forms.EntryForm(data=request.POST)
        if form.is_valid():
            new_entry_save = form.save(commit=False)
            new_entry_save.topic = topic_context
            new_entry_save.save()
            return redirect('log_app:topic', topic_id=topic_id)

    context = {'form': form, 'topic': topic_context}
    return render(request, 'log_app/new_entry.html', context=context)


@login_required
def edit_entry(request, entry_id):
    entry = models.Entry.objects.get(id=entry_id)
    topic_context = entry.topic
    if topic_context.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = forms.EntryForm(instance=entry)
    else:
        form = forms.EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_app:topic', topic_id=topic_context.id)

    context = {'entry': entry, 'topic': topic_context, 'form': form}
    return render(request, 'log_app/edit_entry.html', context=context)
