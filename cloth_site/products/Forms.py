from django import forms
from django.forms import fields
from products.models import products
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class insertProductForm(forms.ModelForm):
    class Meta :
        model = products
        fields = [
            'product_id',
            'name',
            'sell_price',
            'buy_price',
            'num_of_items' ,
            'factory_name'
        ]

class sellForm(forms.Form):
    pay = forms.DecimalField(max_digits=19, decimal_places=10  )
    product_id = forms.CharField( max_length=100)



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username',  'password1', 'password2']