from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html', context)

#def page(request):
#    return HttpResponse('<h1>Page Home</h1>')

def page(request):
    return render(request,'blog/page.html')

#def about(request):
#    return HttpResponse('<h1>About Home</h1>')

def about(request):
    return render(request,'blog/about.html', {'title':'About'})