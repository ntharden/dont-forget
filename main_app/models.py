from django.db import models

# Create your models here.
class Topic(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField(max_length=300)
	# category = models.CharField(max_length=250)
	# notion_url = models.CharField(max_length=250)
	# youtube_url = models.CharField(max_length=250)

	def __str__(self):
		return self.name