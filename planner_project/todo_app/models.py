from django.db import models
from django.contrib.auth.models import User

class TodoModel(models.Model):
	task = models.TextField()
	deadline = models.CharField(max_length=50)
	note = models.TextField(max_length=50, default="NA")
	timestamp = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.task
