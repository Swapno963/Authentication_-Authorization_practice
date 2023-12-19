from django.shortcuts import render
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.
def home(request):
    print(request.POST)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Created Successfully')
            messages.warning(request, 'Account Created Successfully, Warning')
            messages.info(request, 'Account Created Successfully, Info')

            form.save()
    else:
        form = RegisterForm()
    return render(request,'home.html', {'form':form})