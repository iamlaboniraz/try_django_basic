from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
	print(args,kwargs)
	print(request.user)
	#return HttpResponse("<h1>Hello world</h1>")
	return render(request,"home.html")


def contact_view(request,*args,**kwargs):
	return render(request,"contact.html")

def about_view(request,*args,**kwargs):
	my_context={
	  "title":"abc try django project",
	  "my_number":123,
	  "my_list":[123,4242,34567,"ABC"],
	  "my_html":"<h1>Hello World</h1>"
	}
	return render(request,"about.html",my_context)

def social_view(request,*args,**kwargs):
	return render(request,"social.html")		

