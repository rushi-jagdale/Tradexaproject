from django.urls import path
from productapp import views
urlpatterns = [
   
    path('',views.addproduct,name='addproduct')
   
]
