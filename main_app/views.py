from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def topics_index(request):
	topics = Topic.objects.all()
	return render(request, 'topics/index.html', { 'topics':topics })

def topics_detail(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	return render(request, 'topics/detail.html', { 'topic': topic })