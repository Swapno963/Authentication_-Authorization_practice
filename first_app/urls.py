from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name ='home'),
    path('login/', views.user_login, name ='login'),
    path('profile/', views.user_profile, name ='profile'),
    path('signup/', views.user_signup, name ='signup'),
    path('logout/', views.user_logout, name ='logout'),
    path('pass_change/', views.pass_change, name ='pass_change'),
    path('pass_change2/', views.pass_change2, name ='pass_change2'),
]
