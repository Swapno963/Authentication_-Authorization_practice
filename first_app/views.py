from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages

# for login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout


# Create your views here.
def home(request):
    print(request.POST)
    return render(request,'home.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_pass)
                # print('user is :',user)
                if user is not None:
                    login(request, user)
                    return redirect('profile')    
        else: 
            form = AuthenticationForm()
        return render(request, 'login.html',{'form':form})
    else:
        return redirect('profile')

def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html',{'user':request.user})
    else:
        return redirect('login')

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account Created Successfully')
                messages.warning(request, 'Account Created Successfully, Warning')
                messages.info(request, 'Account Created Successfully, Info')

                form.save()
        else:
            form = RegisterForm()
        return render(request, 'signup.html', {'form':form})
    else:
        return redirect('profile')

def user_logout(request):
    logout(request)
    return redirect('login')