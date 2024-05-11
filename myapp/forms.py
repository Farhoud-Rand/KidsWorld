from django import forms
from .models import Story
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, UserChangeForm
from django.contrib.auth.models import User

# Form to add new parking in admin panel
class StoryAdminForm(forms.ModelForm):
    class Meta:
        model = Story
        exclude = ['created_at', 'updated_at', 'users_who_like']  
    
# Form to add new user (register)
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Make email field required

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }

    # Validation Function
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email', "This email is already registered")

        if len(username) < 2:
            self.add_error('username', "Username should be at least 2 characters")

        return cleaned_data
    
    # Hash the password before save it
    def save(self, commit=True):
        # Hash the user's password on save
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

# Form to login the user
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

# Form to update user profile
class UpdateProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        # Override widget attributes for form fields
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control p-2', 'placeholder': 'Username'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control p-2', 'placeholder': 'Email', 'required': True})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = self.instance
        if User.objects.filter(email=email).exclude(pk=user.pk).exists():
            raise forms.ValidationError("This email is already registered")
        return email

# Form to update user password
class UpdatePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(UpdatePasswordForm, self).__init__(*args, **kwargs)
        # Override widget attributes for form fields
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={'class': 'form-control p-2', 'placeholder': 'Password'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={'class': 'form-control p-2', 'placeholder': 'Confirm Password'})