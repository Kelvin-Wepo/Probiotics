from django.shortcuts import redirect, render
from django.http import request
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import logout

from .forms import CustomUserCreationForm

# Create your views here.




class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'




def logout_view(request):
    logout(request)
    return redirect('home.html')

