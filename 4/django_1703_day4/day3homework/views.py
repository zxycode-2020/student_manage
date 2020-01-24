from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    context = {
        'index' : 'active'
    }
    return render(request,'homework/index.html',context)

def manage(request):
    context = {
        'manage' : 'active'
    }
    return render(request,'homework/manage.html',context)

def config(request):
    context = {
        'config' : 'active'
    }
    return render(request,'homework/config.html',context)