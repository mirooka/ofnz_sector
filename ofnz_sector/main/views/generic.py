from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
# from ofnz_sector.accounts.models import Profile
from ofnz_sector.common.view_mixins import RedirectToIndex
from ofnz_sector.main.models import AbstractModel, Shoes, Pants, Shirt, Hat, Jacket


class HomeViewPublic(RedirectToIndex, views.TemplateView):
    template_name = 'main/home_page_no_profile.html'


class HomeViewPrivate(auth_mixins.LoginRequiredMixin, views.ListView):
    template_name = 'main/home_page_with_profile.html'
    model = AbstractModel
    context_object_name = 'products'


class ViewAllProducts(auth_mixins.LoginRequiredMixin, views.ListView):
    template_name = 'main/view_all_products.html'
    model = AbstractModel
    context_object_name = 'products'


class AddProductListView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    template_name = 'main/add_product.html'


class WomenProducts(views.ListView):
    template_name = 'main/list_products.html'
    model = AbstractModel
    context_object_name = 'products'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products_shoes = list(Shoes.objects.all().filter(gender='Female'))
        products_pants = list(Pants.objects.all().filter(gender='Female'))
        products_shirt = list(Shirt.objects.all().filter(gender='Female'))
        products_hat = list(Hat.objects.all().filter(gender='Female'))
        products_jacket = list(Jacket.objects.all().filter(gender='Female'))
        context.update(
            {
                'products_shoes': products_shoes,
                'products_pants': products_pants,
                'products_shirt': products_shirt,
                'products_hat': products_hat,
                'products_jacket': products_jacket,
                # 'is_owner': self.object.user_id == self.request.user.id,
            }
        )
        return context


class MenProducts(views.ListView):
    template_name = 'main/list_products.html'
    model = AbstractModel
    context_object_name = 'products'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products_shoes = list(Shoes.objects.all().filter(gender='Male'))
        products_pants = list(Pants.objects.all().filter(gender='Male'))
        products_shirt = list(Shirt.objects.all().filter(gender='Male'))
        products_hat = list(Hat.objects.all().filter(gender='Male'))
        products_jacket = list(Jacket.objects.all().filter(gender='Male'))
        context.update(
            {
                'products_shoes': products_shoes,
                'products_pants': products_pants,
                'products_shirt': products_shirt,
                'products_hat': products_hat,
                'products_jacket': products_jacket,
                # 'is_owner': self.object.user_id == self.request.user.id,
            }
        )
        return context


class KidsProducts(views.ListView):
    template_name = 'main/list_products.html'
    model = AbstractModel
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products_shoes = list(Shoes.objects.all().filter(gender='Kids'))
        products_pants = list(Pants.objects.all().filter(gender='Kids'))
        products_shirt = list(Shirt.objects.all().filter(gender='Kids'))
        products_hat = list(Hat.objects.all().filter(gender='Kids'))
        products_jacket = list(Jacket.objects.all().filter(gender='Kids'))
        context.update(
            {
                'products_shoes': products_shoes,
                'products_pants': products_pants,
                'products_shirt': products_shirt,
                'products_hat': products_hat,
                'products_jacket': products_jacket,
                # 'is_owner': self.object.user_id == self.request.user.id,
            }
        )
        return context
