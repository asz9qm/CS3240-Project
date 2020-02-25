from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Profile


def display_login(request):
    context = {}
    return render(request, 'login/index.html', context)
    # return redirect('/login/')


@login_required
def make_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserProfileForm({'user': request.user})

    context = {'profile_form': form}
    return render(request, 'login/blank_profile.html', context)


@login_required
def display_profile(request):
    args = {'user': request.user}
    return render(request, 'login/info_profile.html', args)
