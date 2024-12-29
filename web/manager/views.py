from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')    
    else:
        form = RegisterForm()
    
    return render(request, "manager/register.html", {'form': form})

# checks if user is logged in to access this page
@login_required
def profile(request):
    return render(request, "manager/profile.html")