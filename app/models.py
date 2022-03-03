from django.db import models
from django.utils.timezone import  now
from django.contrib.auth.models import User



class Post (models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=30)
	content = models.TextField()
	timeStamp = models.DateTimeField(default=now, blank=True)

	def __str__(self):
		return self.title 

class Contect (models.Model):
	# sno= models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	email= models.CharField(max_length=300)
	phone = models.CharField(max_length=200)
	issu = models.TextField()
	timeStamp= models.DateTimeField(default=now, blank=True)

	def __str__(self):
		return self.name

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	msg = models.TextField()
	
	timeStamp = models.DateTimeField(default=now, blank=True)