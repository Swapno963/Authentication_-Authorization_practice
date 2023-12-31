from django.shortcuts import render,redirect
from .forms import RegisterForm, changeUserData
from django.contrib import messages

# for login
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash


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
        if request.method == 'POST':
            form = changeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Data Chnaged Successfully')
                # messages.warning(request, 'Account Created Successfully, Warning')
                # messages.info(request, 'Account Created Successfully, Info')

                form.save()
        else:
            form = changeUserData(instance=request.user)
        return render(request, 'profile.html', {'form':form})
    else:
        return redirect('signup')

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

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data= request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'passchange.html',{'form':form})
    else:
        return redirect('login')
def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data= request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'passchange.html',{'form':form})
    else:
        return redirect('login')
    

def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = changeUserData(request.POST)
            if form.is_valid():
                messages.success(request, 'Data Chnaged Successfully')
                # messages.warning(request, 'Account Created Successfully, Warning')
                # messages.info(request, 'Account Created Successfully, Info')

                form.save()
        else:
            form = changeUserData()
        return render(request, 'profile.html', {'form':form})
    else:
        return redirect('signup')
