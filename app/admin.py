from django.contrib import admin

# Register your models here.
from app.models import Post
from app.models import Contect
from app.models import Comment
admin.site.register(Post)
admin.site.register(Contect)
admin.site.register(Comment)