from django import forms
from .models import Profile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'major', 'year')

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.major = self.cleaned_data['major']
    #     user.year = self.cleaned_data['year']
    #
    #     if commit:
    #         user.save()
    #     return user

    def save(self, commit=True):
        user = super(UserProfileForm, self).save(commit=False)
        user.major = self.cleaned_data['major']
        user.year = self.cleaned_data['year']
        # if commit:
        user.save()
        return user
