from django.views import generic as views

from ofnz_sector.main.models import AbstractModel


class HomeViewPublic(views.TemplateView):
    template_name = 'main/home_page_no_profile.html'


class HomeViewPrivate(views.ListView):
    template_name = 'main/home_page_with_profile.html'
    model = AbstractModel
    context_object_name = 'products'

class AddProductListView(views.TemplateView):
    template_name = 'main/add_product.html'
