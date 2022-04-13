from django.urls import path

from ofnz_sector.main.views.generic import HomeView, AddProductListView
from ofnz_sector.main.views.products import AddShoesView, AddPantsView, AddShirtView, AddHatView, AddJacketView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('add_product/', AddProductListView.as_view(), name='add product'),
    path('add_product/shoes/', AddShoesView.as_view(), name='add shoes'),
    path('add_product/pants/', AddPantsView.as_view(), name='add pants'),
    path('add_product/shirt/', AddShirtView.as_view(), name='add shirt'),
    path('add_product/hat/', AddHatView.as_view(), name='add hat'),
    path('add_product/jacket/', AddJacketView.as_view(), name='add jacket'),
)
