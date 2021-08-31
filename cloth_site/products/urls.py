from django.contrib import admin
from products import  views
from django.urls import include, path

from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('' , views.checkLogin , name = "login") , 
    path('logout/', views.logoutUser, name="logout"),
    path('solds/' , views.solds , name = "sell") , 
    path('barcode/' , views.barcode , name="barcode") ,
    path('view_profit_/' , views.view_profit , name="view_profit_") ,
    path ('insertProduct/' , views.insert_products , name= "insertProduct"),
    path ('insert_Inventory/' , views.insert_products_inTheInventory , name= "insert_Inventory"),
    path ('view_Inventory/' , views.view_products_inTheInventory , name= "view_Inventory"),

    path ('view_solds_page/' , views.view_solds_page , name= "view_solds_page"),
    path ('returns_products_page/' , views.Return_product , name= "returns_products_page"),
    path('view_currrent_product' , views.view_current_products , name ="view_currrent_product" ),
    path('delete_product/' , views.delete_product , name = "delete_product") , 
    path('viewBill/' , views.viewBills , name = "viewBills") , 
    path('TaskList/' , views.TaskList , name = "TaskList" ) , 
    path('expenses/' , views.EXpenses , name = "expenses" ) , 
    path('ChangePassword/' , views.changePassword.as_view() , name= "ChangePassword" ),
    path('admin/', admin.site.urls),
]