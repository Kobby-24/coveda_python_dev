from django.shortcuts import render,redirect
from .utils import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required



# Create your views here.


def home(request):
    posts = get_all_posts()
    return render(request, 'index.html', {'posts': posts})

def signup(request):
    if request.method == 'POST':
        return signup_view(request)
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        return login_view(request)
    return render(request, 'login.html')
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
@staff_member_required
def admin_view(request):
    posts = get_all_posts()
    return render(request, 'blog.html', {'posts': posts})


@login_required
@staff_member_required
def addpost_view(request):
    if request.method == 'POST':
        return addpost_view_handler(request)
    return render(request, 'blog.html')

@login_required
@staff_member_required
def editpost_view(request, post_id):
    return edit_post_view_handler(request, post_id)

@login_required
@staff_member_required
def deletepost_view(request, post_id):
    return delete_post_view_handler(request, post_id)