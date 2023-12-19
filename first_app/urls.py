from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name ='home'),
    path('login/', views.user_login, name ='login'),
    path('profile/', views.user_profile, name ='profile'),
    path('signup/', views.user_signup, name ='signup'),
]
