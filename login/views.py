from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Profile


@login_required
def make_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserProfileForm({'user': request.user}) # form = UserProfileForm({'user': request.user})  # UserProfileForm(instance=request.user.profile)

    context = {'profile_form': form}
    return render(request, 'login/blank_profile.html', context)


@login_required
def display_profile(request):
    args = {'user': request.user}
    return render(request, 'login/info_profile.html', args)

# def profile(request)


# @login_required
# def get_profile(request):
#     # profile = Profile.objects.get(user=request.user)
#     # context = {
#     #     'profile': profile
#     # }
#     template = 'login/info_profile.html'
#     return render(request, template) #context)