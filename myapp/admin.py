from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from .models import Story
from .forms import StoryAdminForm

# Customize the fields to be displayed when adding a new park
class StoryAdmin(admin.ModelAdmin):
    form = StoryAdminForm
    search_fields = ['id','title','genre', 'age_limit'] # Allow search by these fields

    list_display = ['id','title','genre', 'age_limit','created_at','updated_at'] 
    
# Register your Story model with custom StoryAdmin
admin.site.register(Story, StoryAdmin)

# Optionally, if you want to customize the User model admin
admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass

