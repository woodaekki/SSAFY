from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods, require_POST, require_safe

from .forms import CustomUserCreationForm
from .models import User, Favorite


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('contentfetch:stock_finder')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('contentfetch:stock_finder')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


@login_required
@require_POST
def logout(request):
    auth_logout(request)
    return redirect('contentfetch:stock_finder')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('contentfetch:stock_finder')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contentfetch:stock_finder')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)


@require_safe
def detail(request, user_pk):
    user = User.objects.get(pk=user_pk)

    favorites = user.favorites.all()

    context = {
        'favorites': favorites,
    }

    return render(request, 'accounts/detail.html', context)


@require_POST
@login_required
def addfavorites(request):
    company_name = request.POST.get('company_name')

    if company_name:
        favorite_exists = Favorite.objects.filter(user=request.user, company_name=company_name).exists()

    if not favorite_exists:
        Favorite.objects.create(
            user=request.user,
            company_name=company_name,
        )

    return redirect('accounts:detail', request.user.pk)


@login_required
@require_POST
def delete_favorite(request, pk):
    favorite = Favorite.objects.get(pk=pk)
    favorite.delete()
    return redirect('accounts:detail', request.user.pk)