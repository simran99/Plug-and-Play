from django.shortcuts import render , reverse ,redirect
from django.http import HttpResponse
from connect.models import worker
from master.models import textJob
from django.contrib.auth import authenticate ,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def index(request):
    workers=worker.objects.all()
    context={'workers':workers}
    return render(request,'master/master.html',context)


def addtext(request):
	if request.method == 'POST':
		text= request.POST['text']
		newtext = textJob(text=text)    
		newtext.save()
	return render(request,'master/addtext.html')	

def login_master(request):
	if request.method == 'POST':
		username="master"
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		print(user)
		if user is not None:
			login(request,user)
			return redirect(reverse('master:index'))
		else:
			return render(request,'master/login.html')	
	else:
		return render(request,'master/login.html')	

def logout_master(request):
	logout(request)
	return redirect(reverse('master:login_master'))			




			

