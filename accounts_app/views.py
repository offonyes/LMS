from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm

def login_register(request):
    login_form = LoginForm()
    register_form = RegisterForm()
    
    if request.method == 'POST':
        if 'login' in request.POST:
            print(request.POST)
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        elif 'register' in request.POST:
            print(request.POST)
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                print(register_form)
                user = register_form.save()
                login(request, user)
                return redirect('home')
    print({'login_form': login_form, 'register_form': register_form})
    return render(request, 'index.html', {'login_form': login_form, 'register_form': register_form})

def redirecting_view(request):
    return render(request, 'universities_app/home.html')
