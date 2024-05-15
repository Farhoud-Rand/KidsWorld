from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template
from . import models


# About us page 
# This function renders about us page 
def about_view(request):
    return render(request,"about.html")

# Register page
# This function handles user registration
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user
            return JsonResponse({'success': True})  # Return success response
        else:
            errors = {field: [error for error in errors] for field, errors in form.errors.items()}
            return JsonResponse(errors, status=400)  # Return validation errors as JSON
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# Login page
# This function handles user login    
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully.')
                return JsonResponse({'success': True})
        messages.error(request, 'Invalid username or password.')
        return JsonResponse({'success': False}, status=400)
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

# Logout page
# This function handles user logout
def logout_view(request):
    logout(request)
    return redirect('/login')

# Not login page 
# This function renders the not login page template
def not_login(request):
    return render(request,'not_logged_in.html')

# Profile page
# This function renders the profile form that initially contains user information
@login_required(login_url='/not_login')
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()  
            login(request, user)
            if user is not None:
                return JsonResponse({'success': True})  
            else:
                errors = {field: [error for error in errors] for field, errors in form.errors.items()}
                return JsonResponse(errors, status=400)  
        else:
            errors = {field: [error for error in errors] for field, errors in form.errors.items()}
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = UpdateProfileForm(instance=user)  
    return render(request, "profile.html", {'form': form})

# Profile page
# This function renders the password form that allows user to change its form
@login_required(login_url='/not_login')
def update_password(request):
    user = request.user
    if request.method == 'POST':
        form = UpdatePasswordForm(user, request.POST)
        if form.is_valid():
            form.save()  
            login(request, user)
            if user is not None:
                return JsonResponse({'success': True})  
            else:
                return JsonResponse({'success': False, 'errors': 'Authentication failed'}, status=400)
        else:
            errors = form.errors
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = UpdatePasswordForm(user)  
    return render(request, "update_password.html", {'form':form})

# Contact us page 
# This function renders contact us page that allows users to send email to us
def contact_view(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        name = request.POST.get('name', '')
        msg_subject = request.POST.get('msg_subject', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone_number', '')

        if message and name and msg_subject and email:
            try:
                email_template = get_template('contact_us_email.html')
                context = {
                    'name': name,
                    'email': email,
                    'subject': msg_subject,
                    'phone_number': phone_number,
                    'message': message
                }
                send_mail(
                    msg_subject,
                    message,
                    email,
                    settings.RECEIVERS_EMAILS,
                    fail_silently=False,
                    html_message=email_template.render(context)
                )
                return JsonResponse({'success': True})  # Return success response
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})  # Return error response
        else:
            return JsonResponse({'success': False, 'error': 'All fields are required.'})
    return render(request, 'contact.html')

# Home page 
# This function renders home page 
@login_required(login_url='/not_login')
def home_view(request):
    # Call the get_last_three() function to retrieve the last three added stories
    last_three_stories = models.Story.get_last_three()
    all_stories = models.Story.get_all_stories()
    return render(request, 'home.html', {'last_three_stories': last_three_stories, 'all_stories': all_stories})

# Home Page
#This function to search stories with AJAX
@login_required(login_url='/not_login')
def search_stories(request):
    if request.method == 'POST':
        print(request.POST)
        title = request.POST.get('title')
        stories = Story.objects.filter(title__contains=title)
        print(stories)
        context = {
            "all_stories" : stories
        }
        serilized_stories = Story.serialize_stories(stories)
        return render(request, 'stories_lists.html', context)

# Home page
# This function add specific story to the user's favorite list or remove it from the list
@login_required(login_url='/not_login')
def toggle_favorite(request, story_id):
    if request.method == "POST":
        story = models.Story.objects.get(pk=story_id)
        user = request.user
        if user in story.users_who_like.all():
            # If user has already liked the story, remove it from favorites
            story.users_who_like.remove(user)
            liked = False
        else:
            # If user hasn't liked the story, add it to favorites
            story.users_who_like.add(user)
            liked = True
        return JsonResponse({'liked': liked})

# Favorite list page
# This function renders favorite list page that allows users to remove stories from list and to show these stories
@login_required(login_url='/not_login')
def favorite_list(request):
    favorite_stories = request.user.favorite_stories.all()
    return render(request, 'favorite_list.html', {'favorite_stories': favorite_stories})

# this function to render to story_details page
@login_required(login_url='/not_login')
def story_details(request, story_id):
    story = models.Story.objects.get(id = story_id)
    if request.method == 'POST':
        form = StoryCommentForm(request.POST)
        if form.is_valid():
            form.instance.user_who_comment = request.user
            form.instance.story = models.get_story_by_id(story_id)
            form.save()     
            return JsonResponse({'success': True})  
            
        else:
            errors = {field: [error for error in errors] for field, errors in form.errors.items()}
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = StoryCommentForm()  
    return render(request, 'story_details.html', {'story': story, 'form':form})

# Delete a comment 
def delete_comment(request):
    if request.session['login'] == True:
        if (request.method == 'POST'):
            models.delete_comment(request.POST)
            id = request.POST['id']
            return redirect("/story/"+id)
    else: 
        # Else render a template containing the SweetAlert message and go back to root route
        return render(request, "story_details.html")