from rest_framework import serializers
from products.models import dialyIncome, products ,Expenses,dialyProfit, sold_products ,stat , books  , monthly_profit , Returns_products , bills , customer_note , Expenses_details ,products_inTheInVentory

from rest_framework import serializers
from products.models import Task


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = stat
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = '__all__'



class SOLD_product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ('name' , 'sell_price')

class viewSolds_serializer(serializers.ModelSerializer):
    class Meta:
        model = sold_products
        fields = '__all__'


class createSolds_serializer(serializers.ModelSerializer):
    class Meta:
        model = sold_products
        fields =  '__all__'


class viewProfit_serializer(serializers.ModelSerializer):
    class Meta:
        model = monthly_profit
        fields = '__all__'

class addToProfit_serializer(serializers.ModelSerializer):
    class Meta:
        model = monthly_profit
        fields = '__all__'

class viewDailySolds_serializer(serializers.ModelSerializer):
    class Meta:
        model = sold_products
        fields = '__all__'

class returns_serializer(serializers.ModelSerializer):
    class Meta:
        model = Returns_products
        fields = '__all__'

class bills_serializer(serializers.ModelSerializer):
    class Meta:
        model = bills
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields ='__all__'

class note_serializer(serializers.ModelSerializer) :
    class Meta:
        model = customer_note
        fields = '__all__'


class expense_serializer(serializers.ModelSerializer) :
    class Meta:
        model = Expenses
        fields = '__all__'


class expenses_details_serializer(serializers.ModelSerializer) :
    class Meta:
        model = Expenses_details
        fields = '__all__'


class products_inTheInVentory_serializer(serializers.ModelSerializer) :
    class Meta:
        model = products_inTheInVentory
        fields = '__all__'

class dialyIncomeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = dialyIncome
        fields = '__all__'


