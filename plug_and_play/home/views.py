from django.shortcuts import render , reverse ,redirect
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

from django.utils import timezone


def home(request):
	return render(request,'home/index.html')

def about(request):
	return render(request,'home/about.html')

def contact(request):
	return render(request,'home/contact.html')	