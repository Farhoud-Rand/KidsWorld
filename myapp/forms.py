from django import forms
from .models import Story

# Form to add new parking in admin panel
class StoryAdminForm(forms.ModelForm):
    class Meta:
        model = Story
        exclude = ['created_at', 'updated_at', 'users_who_like']  
    