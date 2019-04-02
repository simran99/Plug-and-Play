from django.shortcuts import render , reverse ,redirect
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

from .models import worker

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
			print(request.session['ip'])
			return redirect(reverse('connect:dashboard'))  
		else:
			messages.add_message(request, messages.ERROR, 'Invalid password')
			return render(request,'connect/login.html')	
	else:
		return render(request,'connect/login.html')	
			

def dashboard(request):
	if request.session['ip']==None:
		redirect(reverse('connect:login'))

	# x_forward_for = request.META.get('HTTP_X_FORWARDED_FOR')
	# ip = request.META.get('HTTP_X_FORWARDED_FOR')
	# if x_forward_for:
	# 	ip = x_forward_for.split(',')[0]
	# else:
	#     ip = request.META.get('REMOTE_ADDR')

	worker_node = worker(worker_ip=request.session['ip'],last_ping=timezone.now() , status=1)    
	worker_node.save()
	# request.session['id']=worker_node.id
	return render(request,'connect/dashboard.html')

def logout_view(request):
	worker.objects.filter(worker_ip=request.session['ip']).delete()
	logout(request)
	return redirect(reverse('connect:login'))


	