from django.db import reset_queries
from django.shortcuts import render , redirect
from django.contrib import messages
from products.Forms import  sellForm , insertProductForm
from products.models import products , sold_products , Profit , products_inTheInVentory , Expenses , dialyProfit , dialyIncome,books,stat
import datetime 
from .decorator import unauthenticated_user , admin_only
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView 
from django.contrib.auth.forms import PasswordChangeForm 
from django.urls import reverse_lazy


@unauthenticated_user
def checkLogin(request) :

    if request.method == 'POST':
        user_pass = request.POST.get('user_pass')
        user_name = request.POST.get('user_name')
        user = authenticate(request, username=user_name, password=user_pass)
        if user is not None:
                login(request, user)
                return redirect('sell')
        else : print ("user name is wrong ")
       

    return render(request ,'login.html' )



def logoutUser(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
@admin_only
def insert_products(request):

    if request.method == 'POST':
        id = request.POST.get('product_id')
        print(id)
        item_name = request.POST.get('name')
        print(item_name)
        sell_price = request.POST.get('sell_price')
        buy_price = request.POST.get('buy_price')
        item_sort = request.POST.get('sort')
        print(item_sort)
        product_count = request.POST.get('num_of_items')
        bookOrStat = request.POST.get('whichPlace')
        profit = int(sell_price) - int(buy_price)
        
        if(bookOrStat == 'book'):

            try:
                already_exsit = books.objects.get(product_id = id)
                print("iam here")
                if item_name == '':
                    already_exsit.num_of_items +=int(product_count)
                    already_exsit.save()         
                    messages.success(request, 'تم زيادة عدد البضاعة بنجاح  ')
                else :
                    print("iam in else ")
                    
            except:
                print("iam here in except")
                q = books(product_id = id , name = item_name  ,sell_price = sell_price , buy_price = buy_price , num_of_items = product_count , profit = profit , sort=item_sort)
                q.save()
                messages.success(request, 'تم إضـافة البضاعة بنجاح  ')
        
        
        else :
            try:
                    IncreaseNumOfStat(request , item_name , product_count)
                    
            except:
                q = stat(product_id = id , name = item_name  ,sell_price = sell_price , buy_price = buy_price , num_of_items = product_count , profit = profit , sort=item_sort)
                q.save()
                messages.success(request, 'تم إضـافة البضاعة بنجاح  ')

        return redirect('insert_products')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = insertProductForm()
    return render(request, 'data_form.html', {'form': form} )


def IncreaseNumOfbooks(request , name , product_count ):
    try:
        already_exsit = books.objects.get(product_id = id)
        if name == '':
            already_exsit.num_of_items +=int(product_count)
            already_exsit.save()         
            messages.success(request, 'تم زيادة عدد البضاعة بنجاح  ')
    except:
        return()
        
        

def IncreaseNumOfStat(request , name , product_count ):
    already_exsit = stat.objects.get(product_id = id)
    if name == '':
        already_exsit.num_of_items +=int(product_count)
        already_exsit.save()         
        messages.success(request, 'تم زيادة عدد البضاعة بنجاح  ')
    



@login_required(login_url='login')
@admin_only
def insert_products_inTheInventory(request):

    if request.method == 'POST':
        id = request.POST.get('product_id')
        name = request.POST.get('name')
        sell_price = request.POST.get('sell_price')
        buy_price = request.POST.get('buy_price')
        factory = request.POST.get('factory_name')
        product_count = request.POST.get('num_of_items')
        print(product_count)
        try:
                already_exsit = products_inTheInVentory.objects.get(product_id = id)
                if name == '':
                    already_exsit.num_of_items +=int(product_count)
                    already_exsit.save()
                    
                    messages.success(request, 'تم زيادة عدد البضاعة بنجاح  ')
                else:
                    messages.success(request, 'لم يتم اضافة البضاعة ، قد يكون  كود المنتج مكرر ، حاول استخدام كود خاص بكل منتج ')
        except:
            q = products_inTheInVentory(product_id = id , name = name  ,sell_price = sell_price , buy_price = buy_price , num_of_items = product_count , factory_name = factory)
            q.save()
            messages.success(request, 'تم إضـافة البضاعة بنجاح  ')


        return redirect('insert_Inventory')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = insertProductForm()
    return render(request, 'insert_Inventory.html', {'form': form} )




@login_required(login_url='login')
def solds(request):
 
    if request.method == 'POST':

        id = request.data.get('product_id')
        num_of_items = request.data.get('num')
        print(num_of_items)
        product_info = products.objects.get(product_id = id)
        product_info.num_of_items -= 1
        product_info.save()
        Sell_price = (product_info.sell_price * int(num_of_items))
        today = datetime.datetime.now()
        date = today.strftime(("%d-%m-%Y    %H:%M:%S"))
        Y_M_D_solds = today.strftime(("%d-%m-%Y"))

        data = {
                    "product_id" : id ,
                    "name" : product_info.name , 
                    "sell_price" : product_info.sell_price , 
                    "sold_date" : date,
                    "year_month_day_solds" : Y_M_D_solds,
                    "num_of_items" : num_of_items,
                }
            
        calculate_profit(product_info.buy_price , product_info.sell_price  ,int(num_of_items) )
        
        return data    
            
    else:
        form = sellForm()
    return render(request, 'sell2.html', {'form': form} )




def calculate_profit(buy_price , sell_price , numOfItems ) :
    profit = (sell_price - buy_price) * numOfItems
    all_price = sell_price * numOfItems
    today = datetime.datetime.now()
    month = today.month
    year = today.year
    day = today.day
    date = str(month) +"-"+str(year)
    date_day = today.strftime(("%d-%m-%Y"))
    print(date_day)
    try:
        q = Profit.objects.get(Date = date)
        q.profit += profit
    except:
        q = Profit(profit = profit , Date = date)
    try:
        s = dialyIncome.objects.get(Date = date_day)
        s.income += all_price
        s.profit += profit
    except:
        s = dialyIncome(Date =date_day  ,income  = all_price , expenses = 0 , profit = profit  )

    q.save()
    s.save()

def returns(id , discount):

            if(discount == ''):
                discount = 0 
            ID = str(id)
            product_info = products.objects.get(product_id = ID)
            product_info.num_of_items += 1
            product_info.save()
            profit = product_info.sell_price - product_info.buy_price
            q = Profit.objects.filter().last()
            s = dialyIncome.objects.filter().last()
            s.income -= (product_info.sell_price - discount)
            s.save()
            q.profit -= (profit- discount )
            q.save()
        
        


def Create_customer_note(request) :
    product_id = request.data.get('product_id')
    customer_name = request.data.get('Customer_name')
    product_info = products.objects.get(product_id =product_id)
    today = datetime.datetime.now()
    date = today.strftime(("%d-%m-%Y    %H:%M:%S"))
    DATA = {
        "product_id" : product_id , 
        "Customer_name" : customer_name ,
        "product_name" : product_info.name ,  
        "Date" : date , 
    }
    reduce_num_of_items_byOne(product_id)
    return DATA


def reduce_num_of_items_byOne(product_id):
    product_info = products.objects.get(product_id =product_id)
    product_info.num_of_items -= 1 
    product_info.save()


def store_expenses(expenses , price) :
    today = datetime.datetime.now()
    month = today.month
    year = today.year
    day = today.day
    date_day = today.strftime(("%d-%m-%Y"))
    date = str(month) +"-"+str(year)
    print(month)
    try:
            ex = Expenses.objects.get(month_date = date)
            ex.price += int(price)
            ex.save()
            
    except:
            ex = Expenses(month_date = date , price = int(price))
            ex.save()
    try:
        ex = dialyIncome.objects.get(Date = date_day)
        ex.expenses += int(price)
        ex.save()
    except:
        e = dialyIncome(Date = date_day ,income = 0 ,expenses = price ,  profit = 0  )
        e.save()




@login_required(login_url='login')
def Return_product(request):
    return render(request , "returns.html")

@login_required(login_url='login')
def view_current_products(request):
    return render (request , "view_products.html")


@login_required(login_url='login')
def view_solds_page(request):
    return render(request , "view_solds.html")

@login_required(login_url='login')
@admin_only
def delete_product(request):

    return render (request , "delete.html" )

@login_required(login_url='login')
def viewBills(request):
    return render (request , "bills.html" )

@login_required(login_url='login')
def barcode(request):
    return render (request , "barcode.html" )

@login_required(login_url='login')
@admin_only
def view_profit(request):
    return render (request , "view_profit_.html" )


@login_required(login_url='login')
def TaskList (request):
    return render(request , "customersNotes.html")

@login_required(login_url='login')
def EXpenses (request):
    return render(request , "expenses.html")


@login_required(login_url='login')
@admin_only
def view_products_inTheInventory (request):
    return render(request , "view_inventory.html")



class changePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('sell')



