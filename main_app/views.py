from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Topic
from django.urls import reverse

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

class TopicCreate(CreateView):
	model = Topic
	fields = '__all__'
	success_url = '/topics/'

	def __str__(self):
		return self.template_name
		
	def get_absolute_url(self):
		return reverse('topics_detail', kwargs={'topic_id': self.id})