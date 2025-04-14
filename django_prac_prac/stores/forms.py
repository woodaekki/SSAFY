from django import forms
from .models import Store, Product

class StorForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
