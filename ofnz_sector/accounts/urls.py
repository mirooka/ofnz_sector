from django.urls import path
from django.views.generic import RedirectView

from ofnz_sector.accounts.views import UserLoginView, ChangeUserPasswordView, ProfileDetailsView, UserRegisterView, \
    ProfileDeleteView, ProfileEditView, UserLogoutView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('edit-pass/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password-change-done/', RedirectView.as_view(), name='change password done'),

    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('register/', UserRegisterView.as_view(), name='profile register'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile edit'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='profile delete'),
)
