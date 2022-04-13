from django.views import generic as views


class HomeView(views.TemplateView):
    template_name = 'main/home_page.html'


class AddProductListView(views.TemplateView):
    template_name = 'main/add_product.html'
