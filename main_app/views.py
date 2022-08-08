from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Topic:
	def __init__(self, name, description):
		self.name = name
		self.description = description

topics = [
	Topic('Template Literals', 'Template literals are part of the ES2015 specification. They are another way to define and use strings in JavaScript.'),
	Topic('Functional Programming', 'Functional Programming (FP) is the process of building software by composing pure functions, avoiding shared state, mutable data, and side effects. FP is also declarative rather than imperative, and application state flows through pure functions. With Object Oriented Programming (OOP), application state is usually shared and co-located with methods in objects.'),
	Topic('MUI & React Forms', 'The React UI library you always wanted.'),
]

def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

def topics_index(request):
  return render(request, 'topics/index.html', { 'topics':topics })