from django.contrib import admin
from api import  views
from django.urls import  path


urlpatterns = [
    path('view/' , views.view_products , name = "view") ,
    path('viewInventory/' , views.view_productsInInventory , name = "viewInventory") ,
    path('create_sold_product/' , views.create_sold_product , name ="create_sold_product" ),
    path('view_sold_product/' , views.view_solds , name ="view_sold_product" ),
    path('view_daily_solds/' , views.view_daily_solds , name ="view_daily_solds" ),
    path('view_profit/' , views.view_profit , name ="view_profit" ),
    path('reduce_profit_by_discount/' , views.reduce_profit_by_discount , name ="reduce_profit_by_discount" ),
    path('returns_products/' , views.returns_products , name ="returns_products" ),
    path('product-delete/<str:pk>/<str:WhichPlace>/', views.productDelete, name="product-delete"),
    path('bills/' , views.putSoldsInBill , name ="bills" ),
    path('DeleteBills/' , views.billsDelete , name ="DeleteBills" ),
    path('create_note/' , views.create_note , name = "create_note") , 
    
    path('view_expenses_details/' , views.view_exepenses_details , name = "view_expenses_details") ,
    path('create_expenses/' , views.monthly_expenses , name = "create_expenses") ,
    path('DialyIncome/' , views.DialyIncome , name = "DialyIncome") ,
    path('ShowDialyIncome/' , views.ShowDialyIncome , name = "ShowDialyIncome") ,
    
    path('note-delete/<str:pk>/', views.Delete_note, name="note-delete"),
     
]

