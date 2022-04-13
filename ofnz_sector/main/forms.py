from django import forms

from ofnz_sector.common.helpers import BootstrapFormMixin
from ofnz_sector.main.models import Shoes, Pants, Shirt, Hat, Jacket


class CreateProductForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        product = super().save(commit=False)
        product.user = self.user
        if commit:
            product.save()
        return product


class CreateShoesForm(CreateProductForm):
    class Meta:
        model = Shoes
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter title of product',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter picture url'
                }
            )
        }


class CreatePantsForm(CreateProductForm):
    class Meta:
        model = Pants
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter title of product',
                }
            ),
        }


class CreateShirtForm(CreateProductForm):
    class Meta:
        model = Shirt
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter title of product',
                }
            ),
        }


class CreateHatForm(CreateProductForm):
    class Meta:
        model = Hat
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter title of product',
                }
            ),
        }


class CreateJacketForm(CreateProductForm):
    class Meta:
        model = Jacket
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter title of product',
                }
            ),
        }
