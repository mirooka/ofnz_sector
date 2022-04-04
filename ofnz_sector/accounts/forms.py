from django import forms

from ofnz_sector.accounts.models import Profile
from ofnz_sector.common.helpers import BootstrapFormMixin
from django.contrib.auth import forms as auth_forms, get_user_model


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH
    )
    picture = forms.URLField()
    date_of_birth = forms.DateField()
    gender = forms.ChoiceField(
        choices=Profile.GENDERS
    )
    email = forms.EmailField

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            gender=self.cleaned_data['gender'],
            email=self.cleaned_data['email'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'picture')

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
        }
