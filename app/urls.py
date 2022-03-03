from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   path('',views.home, name='home'),
   path("signup/",views.signup, name= 'signup'),
   path('login/', views.login,name="login"),
   path('blogs/<int:id>/',views.blog, name= 'blog_name'),
   path('comment/<int:id>/',views.comment,name='comment'),
   path('home/',views.bloghome,name='bloghome'),
   path('contect/', views.contect,name='contect'),
   path('addblog/',views.addblog,name='addblog')
]
