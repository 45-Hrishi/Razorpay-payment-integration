from django.contrib import admin
from django.urls import path,include
from .import views
app_name = 'payment'
urlpatterns = [
    path('',views.home,name='home'),
    path('donate/',views.donate,name='donate'),
    path('success/',views.success,name='success'),
]