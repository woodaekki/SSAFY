from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

User = get_user_model()
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("boards:index")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('boards:index')

@login_required
def profile(request, pk):
    user_user = User.objects.get(pk=pk)
    boards = user_user.board_set.all()
    comments = user_user.comment_set.all()
    context = {
        'user_user' : user_user,
        'boards': boards,
        'comments': comments,
    }

    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, user_pk) : 
    User = get_user_model()
    user = User.objects.get(pk = user_pk)
    if request.user in user.followers.all() : 
        user.followers.remove(request.user)
    else : 
        user.followers.add(request.user)
    return redirect('accounts:profile', user_pk)