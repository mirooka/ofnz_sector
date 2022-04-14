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
        fields = ('title', 'gender', 'picture', 'type', 'price', 'description')
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
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3,
                }
            ),
        }


class CreatePantsForm(CreateProductForm):
    class Meta:
        model = Pants
        fields = ('title', 'gender', 'picture', 'type', 'price', 'description')
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
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3,
                }
            ),
        }


class CreateShirtForm(CreateProductForm):
    class Meta:
        model = Shirt
        fields = ('title', 'gender', 'picture', 'type', 'price', 'description')
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
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3,
                }
            ),
        }


class CreateHatForm(CreateProductForm):
    class Meta:
        model = Hat
        fields = ('title', 'gender', 'picture', 'type', 'price', 'description')
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
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3,
                }
            ),
        }


class CreateJacketForm(CreateProductForm):
    class Meta:
        model = Jacket
        fields = ('title', 'gender', 'picture', 'type', 'price', 'description')
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
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3,
                }
            ),
        }
