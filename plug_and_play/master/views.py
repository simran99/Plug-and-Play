from django.shortcuts import render , reverse ,redirect
from django.http import HttpResponse
from connect.models import worker
from master.models import textJob

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

