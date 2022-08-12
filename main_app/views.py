from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Topic
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def topics_index(request):
	topics = Topic.objects.filter(user=request.user)
	return render(request, 'topics/index.html', { 'topics':topics })

@login_required
def topics_detail(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	return render(request, 'topics/detail.html', { 'topic': topic })

class TopicCreate(LoginRequiredMixin, CreateView):
	model = Topic
	fields = '__all__'
	success_url = '/topics/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def __str__(self):
		return self.template_name
		
	def get_absolute_url(self):
		return reverse('topics_detail', kwargs={'topic_id': self.id})

class TopicUpdate(LoginRequiredMixin, UpdateView):
  model = Topic
  fields = '__all__'
  success_url = '/topics/'

class TopicDelete(LoginRequiredMixin, DeleteView):
  model = Topic
  success_url = '/topics/'

class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)