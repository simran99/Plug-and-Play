
# Create your views here.
from django.shortcuts import render , reverse ,redirect
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from background_task import background
from connect.models import worker
from master.models import textJob
import time
from django.utils import timezone

def index(request):
	x_forward_for = request.META.get('HTTP_X_FORWARDED_FOR')
	ip = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forward_for:
		ip = x_forward_for.split(',')[0]
	else:
	    ip = request.META.get('REMOTE_ADDR')
	check(ip)
	return HttpResponse("CHECKING")


@background(schedule=3)
def check(ip):
	print(ip+"   "+time.ctime())
