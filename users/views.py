from django.shortcuts import render, redirect
from django.contrib import messages #for displaying feedback messages ie after successful login
from .forms import UserRegisterForm #using forms for login/register
from django.contrib.auth.decorators import login_required #to require login for specific access ie Profile
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')