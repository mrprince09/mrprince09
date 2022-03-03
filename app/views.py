from django.shortcuts import render , redirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from app.models import Post
from .models import Contect
from .models import Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


from .forms import BlogForm,CommentForm,ContectForm

  

# Create your views here.
def home (request):
	return render(request,"home.html")

def signup(request):
	if request.method=="POST":
		username= request.POST['uname']
		password= request.POST['password']
		myuser=User(username=username)

		myuser.set_password(password)
		myuser.save()

		
		
		return redirect('login')
	else:	
		return render(request,"signup.html")

def login(request):

	if request.method=='POST':
		# import pdb;pdb.set_trace()

		
		username= request.POST['uname']
		password= request.POST['password']
		# import pdb;pdb.set_trace()

		user = authenticate(username=username, password=password)
		if user is not None:
			auth_login(request,user)
			return redirect('bloghome')
		else:
			error={'error':'invalid password'}
			return render(request,'login.html',error)
	else:
		error={'error':'invalid username or password'}
		return render(request,'login.html')

@login_required(redirect_field_name='login')
def blog(request,id):
	form=CommentForm()
	
	blogpost=Post.objects.get(id=id)
	bcomment= Comment.objects.filter(post=blogpost)
	context= {'blogpost': blogpost, "com":bcomment ,"form":form}

	return render(request ,'blogy.html',context)

def comment(request,id):
	
	if request.user.is_authenticated:
		# form=CommentForm()
		if request.method=='POST':
			import pdb;pdb.set_trace()	
			form=CommentForm(request.POST)
			# if form.is_valid():
			obj=form.save(commit=False)
			obj.user=request.user
			obj.post=Post.object.get(id=id)
			# import pdb;pdb.set_trace()
			obj.save()
			return redirect('bloghome')
		
			
			
		

def bloghome (request):

	blogpost=Post.objects.all()
	context= {'blogpost': blogpost}
	return render(request, 'bloghome.html',context)

def contect(request):
	if request.user.is_authenticated:
		form=ContectForm()
		if request.method=="POST":
			form=ContectForm(request.POST)
			if form.is_valid():
				com_obj=form.save(commit=False)
				com_obj.save()
				return redirect ('bloghome')
	return render(request, "contect.html", {"form":form})


def addblog (request):

	if request.user.is_authenticated:
		form=BlogForm()
		if request.method=="POST":
			form=BlogForm(request.POST)
			if form.is_valid():
				bolg_obj=form.save(commit=False)
				bolg_obj.user=request.user
				bolg_obj.save()

			return redirect('bloghome')
		return render(request, "addblog.html",{'form':form})

	return HttpResponseRedirect(reverse('login'))

def logout(request):
	return "dsfsd"
