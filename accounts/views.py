from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm,CustomAuthenticationForm

# Create your views here.
def register(request):
    if request.method != 'POST':
        form = CustomUserCreationForm()
    
    else:
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            auth_login(request, new_user)
            return redirect ("threads:index")

    context = {'form':form}
    return render(request, 'registration/register.html', context)

def login(request):
    if request.method != 'POST':
        form = CustomAuthenticationForm()
    else:
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect ("threads:index")

    context = {'form':form}
    return render(request, 'registration/login.html', context)

