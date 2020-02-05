from django.shortcuts import render
from .models import Topic
from django.views.generic.list import ListView

# Create your views here.
class TopicListView(ListView):
    model = Topic
    template_name = "classview/topics.html"
    context_object_name = 'topics'