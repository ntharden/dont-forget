from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('topics/', views.topics_index, name='topics_index'),
  path('topics/<int:topic_id>/', views.topics_detail, name='topics_detail'),
  path('topics/create/', views.TopicCreate.as_view(), name='topics_create'),
  path('topics/<int:pk>/update/', views.TopicUpdate.as_view(), name='topics_update'),
  path('topics/<int:pk>/delete/', views.TopicDelete.as_view(), name='topics_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]