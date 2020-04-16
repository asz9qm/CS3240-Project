from .forms import UserProfileForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile


def display_login(request):
    context = {}
    return render(request, 'login/index.html', context)



@login_required
def make_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, f'Your account has been created !')
        return redirect('/')
    else:
        form = UserProfileForm({'user': request.user})

    context = {'profile_form': form}
    return render(request, 'login/blank_profile.html', context)


@login_required
def display_profile(request):
    args = {'user': request.user}
    return render(request, 'login/info_profile.html', args)


@login_required
def update_profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated !')
            return redirect('login:display_profile')

    else:
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
    context = { 
        'p_form': p_form
    }

    return render(request, 'login/update_profile.html', context)
