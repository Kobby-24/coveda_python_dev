from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .models import AuthUser,blogPost
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()


## Login View
def login_view(request):
    login_ = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user_obj = User.objects.get(email=login_)
        user = authenticate(username=user_obj.username, password=password)
    except User.DoesNotExist:
    # Fallback: try by username
        user = authenticate(username=login_, password=password)
    
    
    if user is not None:
        login(request, user)
        return redirect('home') # Redirect to home page after login
    else:
        return render(request, 'login.html', {'error': 'Invalid credentials'})
 ## Signup View   
def signup_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    if username and password and email:
        # Check if the username or email already existsif
        try:
            user = User.objects.create_user(
                first_name='',
                last_name='',
                username=username,
                email=email,
                password=password,
                is_staff=False,
                is_superuser=False
            )
            user.save()
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'Username or email already taken'})
            # Handle the case where the
            # IntegrityError is raised if a
        # user with the given username or email already exists


        login(request, user)
        from django.contrib import messages
        messages.success(request, 'Account created successfully')
        return redirect('home')
    else:
        return render(request, 'signup.html', {'error': 'Please fill all fields'})
    
    
def password_reset_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            # Here you would typically send an email with a password reset link
            # For simplicity, we will just render a success message
            return render(request, 'password_reset.html', {'message': 'Password reset link sent to your email'})
        except User.DoesNotExist:
            return render(request, 'password_reset.html', {'error': 'Email not found'})
    return render(request, 'password_reset.html')



def addpost_view_handler(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user  # Assuming the user is logged in
        
        # Validate the input
        if not title or not content:
            return render(request, 'blog.html', {'error': 'Please fill all required fields'})
        
        if title and content and author:
            # Create and save the post to the database
            post = blogPost(title=title, content=content, author=author)
            post.save()
            return render(request, 'blog.html', {'success_message': 'Post added successfully'})
    
    return render(request, 'blog.html')

def edit_post_view_handler(request, post_id):
    try:
        post = blogPost.objects.get(id=post_id)
    except blogPost.DoesNotExist:
        return render(request, 'blog.html', {'error': 'Post not found'})
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return render(request, 'blog.html', {'success_message': 'Post updated successfully', 'post': post})
    
    return render(request, 'blog.html', {'post': post, 'edit_mode': True})

def delete_post_view_handler(request, post_id):
    try:
        post = blogPost.objects.get(id=post_id)
    except blogPost.DoesNotExist:
        return render(request, 'blog.html', {'error': 'Post not found'})
    
    if request.method == 'POST':
        post.delete()
        return redirect('admin_view')  # Redirect to admin view after deleting
    
    return render(request, 'blog.html', {'post': post, 'delete_mode': True})

def get_all_posts():
    posts = blogPost.objects.all().order_by('-created_at')
    posts_list  = list(posts)  # Convert QuerySet to list for easier manipulation
    for post in posts:
        post.author_name = post.author.username if post.author else 'Unknown'  
    return posts_list

