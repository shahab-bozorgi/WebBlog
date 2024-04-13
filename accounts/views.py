from django.shortcuts import render , redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, UserEditForm


def login_user (request):
    if request.user.is_authenticated == True:
        return redirect('home_app:main')

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            user = User.objects.get(username=form.cleaned_data['username'])
            login(request, user)

            return redirect('home_app:main')
        else:
            form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_register(request):
    context = {'Errors':[]}
    if request.user.is_authenticated == True:
        return redirect('home_app:main')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            context['Errors'].append("Passwords are not the same")
            return render(request, 'accounts/register.html', context)

        user = User.objects.create(username=username, email=email, password=password1)
        login(request, user)
        return redirect('home_app:main')
    return render(request, 'accounts/register.html')


def user_edit(request):

    form = UserEditForm(instance=request.user)
    if request.method == 'POST':
        form = UserEditForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    return render(request, 'accounts/edit.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home_app:main')


