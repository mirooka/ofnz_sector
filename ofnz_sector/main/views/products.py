from django.views import generic as views
from django.urls import reverse_lazy

from ofnz_sector.main.forms import CreateShoesForm, CreateJacketForm, CreateHatForm, CreateShirtForm, CreatePantsForm


class AddShoesView(views.CreateView):
    form_class = CreateShoesForm
    template_name = 'main/add_shoes.html'
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AddPantsView(views.CreateView):
    form_class = CreatePantsForm
    template_name = 'main/add_pants.html'
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AddShirtView(views.CreateView):
    form_class = CreateShirtForm
    template_name = 'main/add_shirt.html'
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AddHatView(views.CreateView):
    form_class = CreateHatForm
    template_name = 'main/add_hat.html'
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AddJacketView(views.CreateView):
    form_class = CreateJacketForm
    template_name = 'main/add_jacket.html'
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs



