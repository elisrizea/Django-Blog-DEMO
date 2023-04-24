
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Posts


# Imports for api
from rest_framework import generics,viewsets
from rest_framework import permissions
from .serializers import PostSerializer,UserSerializer

# Create your views here.
def home(request):
    posts = Posts.objects.all

    context = {'posts': posts, }
    return render(request, 'posts.html', context)

def about(request):
    return render(request,'about.html',{})


def portfolio(request):
    return render(request,'portfolio.html',{})

def posts(request):
    posts=Posts.objects.all().order_by('-date')

    context={'posts':posts,}
    return render(request,'posts.html',context)

def contact(request):
    return render(request,'contact.html',{})

# uncomment line 36 to show 404 error
# when add_post link is requested when user is not logged in instead of asking user to login
#@login_required
def add_post(request):
    sent=False
    add_post_form = PostForm(request.POST or None)
    if add_post_form.is_valid():
        add_post_form.save()
        sent=True
        return redirect('posts')
    context = {'status': sent,'add_post_form': add_post_form}
    return render(request,'add_post.html',context)


class PostApiVewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('-date')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


