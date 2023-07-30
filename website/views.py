from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SingUpForm
from .models import Record
def home(request):
    records = Record.objects.all()
    
    # if login in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'welcome back ' + username + ' you are logged successfully')
            return redirect('home')
        else:
            messages.success(request, 'There was an error to login please try again')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registerition has been done')
            return redirect('home')
    else:
        form = SingUpForm()
        return render(request, 'register.html', {
            'form':form
            })
    return render(request, 'register.html', {'form': form})
