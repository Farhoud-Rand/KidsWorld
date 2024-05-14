from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm, UpdatePasswordForm, UpdateProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template

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