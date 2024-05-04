from django.forms import ModelForm
from .models import ProductsAbout


class ProductForm(ModelForm):
    class Meta:
        model = ProductsAbout
        fields = '__all__'