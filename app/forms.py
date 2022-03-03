
from django.forms import ModelForm
from . models import Post, Comment , Contect


class BlogForm(ModelForm):
	class Meta:
		model=Post
		fields=('title','content')

class CommentForm(ModelForm):
	class Meta:
		model=Comment
		fields=("user","post","msg")


class ContectForm(ModelForm):
	class Meta:
		model=Contect
		fields=("name","email","phone","issu")

