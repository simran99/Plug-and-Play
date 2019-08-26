from django.shortcuts import render , reverse ,redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.conf import settings
from wsgiref.util import FileWrapper
import mimetypes
import os
from django.utils.encoding import smart_str

# Create your views here.
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from background_task import background
import time
from connect.models import worker
from master.models import textJob
from django.utils import timezone


def index(request):
    return redirect(reverse('connect:login'))

def login(request):
	if request.method == 'POST':
		password= request.POST['password']
		
		if password=="abc":
			x_forward_for = request.META.get('HTTP_X_FORWARDED_FOR')
			ip = request.META.get('HTTP_X_FORWARDED_FOR')
			if x_forward_for:
				ip = x_forward_for.split(',')[0]
			else:
			    ip = request.META.get('REMOTE_ADDR')
			request.session['ip'] = ip
			worker_node = worker(worker_ip=request.session['ip'],last_ping=timezone.now() , status=1)    
			worker_node.save()
			return redirect(reverse('connect:dashboard'))  
		else:
			messages.add_message(request, messages.ERROR, 'Invalid password')
			return render(request,'connect/login.html')	
	else:
		return render(request,'connect/login.html')	
			

def dashboard(request):
	if request.session['ip']:
		redirect(reverse('connect:login'))
	check(request.session['ip'])
	return render(request,'connect/dashboard.html')

def showtext(request):
	text= textJob.objects.all()
	context={'text':text}
	return render(request,'connect/showtext.html',context)

def openfile(request):
	return render(request,'connect/openfile.html')

def download(request):
	file_name='check.pdf'
	file_path = settings.MEDIA_ROOT +'/check.pdf'
	file_wrapper = FileWrapper(open(file_path,'rb'))
	file_mimetype = mimetypes.guess_type(file_path)
	response = HttpResponse(file_wrapper, content_type=file_mimetype )
	response['X-Sendfile'] = file_path
	response['Content-Length'] = os.stat(file_path).st_size
	response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name) 
	return response

def logout_view(request):
	worker.objects.filter(worker_ip=request.session['ip']).delete()
	logout(request)
	return redirect(reverse('connect:login'))

@background(schedule=3)
def check(ip):
	# print(ip+"   "+time.ctime())
	print("hello")
