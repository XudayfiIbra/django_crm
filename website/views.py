from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SingUpForm, addRecordForm
from .models import Record

# Home View

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

# Logout View

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


# registertions View

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



# Customer record View

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look the record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {
            'customer_record':customer_record
        })
    else:
        messages.success(request, 'You must logged in to view that page')
        return redirect('home')
    
    

# delete record view

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record has been successfully deleted')
        return redirect('home')
    else:
        messages.success(request, 'You need to login to delete a record')
        return redirect('home')
    
# adding record   
    
def add_record(request):
    form = addRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record was added')
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, 'You must logged in to view that page')
        return redirect('home')


# update record

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = addRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record has been updated')
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, 'You must logged in to view that page')
        return redirect('home')
