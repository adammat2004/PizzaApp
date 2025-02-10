# pizza/forms.py

from django import forms
from django.forms import formset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PizzaOrder, DeliveryDetail, PizzaSize, CrustType, SauceType, CheeseType, Topping

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PizzaOrderForm(forms.ModelForm):
    size = forms.ModelChoiceField(queryset=PizzaSize.objects.all(), empty_label="Select Size")
    crust = forms.ModelChoiceField(queryset=CrustType.objects.all(), empty_label="Select Crust")
    sauce = forms.ModelChoiceField(queryset=SauceType.objects.all(), empty_label="Select Sauce")    
    cheese = forms.ModelChoiceField(queryset=CheeseType.objects.all(), empty_label="Select Cheese")
    toppings = forms.ModelMultipleChoiceField(queryset=Topping.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = PizzaOrder
        fields = ['size', 'crust', 'sauce', 'cheese', 'toppings']
PizzaOrderFormSet = formset_factory(PizzaOrderForm, extra=1, can_delete=True)
    
class DeliveryDetailForm(forms.ModelForm):
    class Meta:
        model = DeliveryDetail
        fields = ['name', 'address', 'card_number', 'card_cvv']

    expiry_month = forms.ChoiceField(choices=[(i, f'{i:02d}') for i in range(1, 13)], label="Expiry Month")
    expiry_year = forms.ChoiceField(choices=[(i, f'{i}') for i in range(2025, 2035)], label="Expiry Year")


    def clean_card_number(self):
        card_number = self.cleaned_data.get('card_number')
        if not card_number or len(card_number) != 16:
            raise forms.ValidationError("Card number must be 16 digits.")
        return card_number

    def clean_card_cvv(self):
        card_cvv = self.cleaned_data.get('card_cvv')
        if not card_cvv or len(card_cvv) != 3:
            raise forms.ValidationError("CVV must be 3 digits.")
        return card_cvv
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        month = self.cleaned_data.get('expiry_month')
        year = self.cleaned_data.get('expiry_year')
        instance.setExpiryDate(month, year)
        if commit:
            instance.save()
        return instance