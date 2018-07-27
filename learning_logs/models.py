from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	text = models.CharField(max_length=200)
	data_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User)

	def __str__(self):
		return self.text

class Entry(models.Model):
	topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
	text = models.TextField()
	data_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		return self.text[:50] + "..."