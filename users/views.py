from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import *
from django.contrib.auth import logout as auth_logout  # Correct import




def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

class CustomLoginView(LoginView):
    form_class = CustomUserCreationForm
    template_name = 'users/login.html'

login_view = CustomLoginView.as_view()

def logout(request):
    auth_logout(request)
    return redirect('users:login')
