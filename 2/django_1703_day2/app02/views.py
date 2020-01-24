from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    return render(request,'app02/index.html')

def test(request):
    return HttpResponse('app02 test ok')

def test_redirect(request):
    try:
        url = reverse('app02:new_test')
    except Exception,e:
        url = '/'
        print str(e)
    return HttpResponseRedirect(url)

def new_test(request):
    return HttpResponse('new test page ok')