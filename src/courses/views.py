from django.shortcuts import render,get_object_or_404
from .models import course
from django.views import View
# Create your views here.
class courseView(View):
	template_name="course_detail.html"
	def get(self,request,id=None,*args,**kwargs):
		context={}
		if id is not None:
			obj=get_object_or_404(course,id=id)
			context['object']=obj
		return render(request,self.template_name,context)	
class courseListView(View):		
	template_name="course_list.html"
	queryset=course.objects.all()
	def get_queryset(self):
		return self.queryset
	def get(self,request,*args,**kwargs):
		context={
		    "object_list":self.get_queryset()
		}
		return render(request,self.template_name,context)