from django.urls import path
from django.views.generic import RedirectView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='Login user'),
    path('edit-pass/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password-change-done/', RedirectView.as_view(), name='change password done'),

    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('register/', ProfileRegisterView.as_view(), name='profile register'),
)
