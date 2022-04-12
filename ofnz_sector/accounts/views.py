from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, logout

# from django.shortcuts import render


# Create your views here.
from ofnz_sector.accounts.forms import CreateProfileForm
from ofnz_sector.accounts.models import Profile


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('index')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


def logout_view(request):
    logout(request)
    return redirect('index')


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # clothes owned by profile
        context.update(
            {
                'is_owner': self.object.user_id == self.request.user.id
            }
        )

        return context


class ProfileEditView(views.UpdateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_edit.html'
    template_name_suffix = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    success_url = reverse_lazy('main/home_page.html')


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/profile_delete.html'
    model = Profile

    def get_object(self, queryset=None):
        profile_object = super(ProfileDeleteView, self).get_object()
        if not profile_object.owner == self.request.user:
            raise Http404
        return profile_object

    template_name_suffix = 'profile'
    success_url = reverse_lazy('index')
