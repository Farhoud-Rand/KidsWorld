from django.urls import path
from . import views

urlpatterns = [
    path('',views.register_view, name='register'),
    path('login/', views.login_view, name='login'),  
    path('logout',views.logout_view),
    path('not_login',views.not_login),
    path('profile/', views.profile_view, name='profile'),
    path('update_password', views.update_password),
    path('contact',views.contact_view, name='contact'),

]
