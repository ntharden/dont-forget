from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField(max_length=300)
	category = models.CharField(max_length=250)
	notion_url = models.CharField(max_length=250)
	youtube_url = models.CharField(max_length=250)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name