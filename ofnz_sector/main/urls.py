from django.urls import path

from ofnz_sector.main.views import HomeView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),

)
