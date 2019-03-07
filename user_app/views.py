from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm


def _register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # return render(request, 'matches:index')
            return redirect('matches:index')
    else:
        form = UserCreationForm()
    return render(request, 'user_app/signup.html', {'form': form})


def _logout(request):
    logout(request)
    return redirect('matches:index')


def _login(request):
    ctx = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('matches:index')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            ctx['login_error'] = 'Wrong login or password'
            return render(request, 'user_app/login.html', ctx)
    else:
        return render(request, 'user_app/login.html', ctx)
