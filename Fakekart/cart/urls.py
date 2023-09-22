from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    
    path('',views.cart_detail,name='cart_detail'),
    path(' add/<int:pro_id>/',views.add_to_cart,name='add_to_cart'),
    path(' remove/<int:pro_id>/',views.cart_remove,name='cart_remove'),
    path(' trash/<int:pro_id>/',views.trash,name='trash'),
]
