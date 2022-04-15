from django.urls import path

from ofnz_sector.main.views.generic import HomeViewPublic, AddProductListView, HomeViewPrivate, WomenProducts, \
    MenProducts, KidsProducts, ViewAllProducts
from ofnz_sector.main.views.products import AddShoesView, AddPantsView, AddShirtView, AddHatView, AddJacketView, \
    ProductDetailView, ProductDeleteView, ProductEditView

urlpatterns = (
    path('home/', HomeViewPublic.as_view(), name='index public'),
    path('', HomeViewPrivate.as_view(), name='index private'),

    path('add_product/', AddProductListView.as_view(), name='add product'),
    path('add_product/shoes/', AddShoesView.as_view(), name='add shoes'),
    path('add_product/pants/', AddPantsView.as_view(), name='add pants'),
    path('add_product/shirt/', AddShirtView.as_view(), name='add shirt'),
    path('add_product/hat/', AddHatView.as_view(), name='add hat'),
    path('add_product/jacket/', AddJacketView.as_view(), name='add jacket'),
    path('details_product/<int:pk>/', ProductDetailView.as_view(), name='details product'),
    path('edit_product/<int:pk>/', ProductEditView.as_view(), name='edit product'),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete product'),

    path('all_products/', ViewAllProducts.as_view(), name='show all products'),
    path('women_products/', WomenProducts.as_view(), name='women products'),
    path('men_products/', MenProducts.as_view(), name='men products'),
    path('kids_products/', KidsProducts.as_view(), name='kids products'),
)
