from django.urls import path
from . import views

urlpatterns = [
    path ('',views.about_view, name='about'),
    path ('about',views.about_view),
    path('register',views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout',views.logout_view, name='logout'),
    path('not_login',views.not_login, name='not_login'),
    path('profile', views.profile_view, name='profile'),
    path('update_password', views.update_password, name='update_password'),
    path('contact',views.contact_view, name='contact'),
    path('home',views.home_view, name='home'),
    path('favorite_list',views.favorite_list, name='favorite_list'),
    path('story/<int:story_id>', views.story_details, name='story_details'),
    path('delete_comment', views.delete_comment, name='delete_comment')

]