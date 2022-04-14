from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, logout

# from django.shortcuts import render


# Create your views here.
from ofnz_sector.accounts.forms import CreateProfileForm, EditProfileForm
from ofnz_sector.accounts.models import Profile
from ofnz_sector.main.models import Shoes, Pants, Shirt, Hat, Jacket


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('index public')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('index private')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    template_name = 'main/home_page_no_profile.html'


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('index private')


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products_shoes = list(Shoes.objects.filter(user_id=self.object.user_id))
        products_pants = list(Pants.objects.filter(user_id=self.object.user_id))
        products_shirt = list(Shirt.objects.filter(user_id=self.object.user_id))
        products_hat = list(Hat.objects.filter(user_id=self.object.user_id))
        products_jacket = list(Jacket.objects.filter(user_id=self.object.user_id))
        context.update(
            {
                'products_shoes': products_shoes,
                'products_pants': products_pants,
                'products_shirt': products_shirt,
                'products_hat': products_hat,
                'products_jacket': products_jacket,
                'is_owner': self.object.user_id == self.request.user.id,
            }
        )

        return context


class ProfileEditView(views.UpdateView):
    form_class = EditProfileForm
    model = Profile
    template_name = 'accounts/profile_edit.html'

    success_url = reverse_lazy('main/home_page_no_profile.html')


class ProfileDeleteView(views.DeleteView):
    model = Profile

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(owner=owner)

    template_name = 'accounts/profile_delete.html'
    template_name_suffix = 'profile'

    success_url = reverse_lazy('index public')
