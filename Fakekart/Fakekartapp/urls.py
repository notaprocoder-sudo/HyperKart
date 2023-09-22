from django.urls import path
from . import views

app_name='Fakekartapp'

urlpatterns = [
    path('', views.AllProdCat , name='AllProdCat'),
    path('<slug:c_slug>/',views.AllProdCat,name='PbyC'),
    path('<slug:p_slug>/', views.prodetail,name='prodetail'),
    path('<slug:c_slug>/<slug:p_slug>/', views.prodetail,name='procatdetail'),
]