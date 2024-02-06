from django.contrib import admin
from django.urls import path
from MYAPP import views

urlpatterns = [
   path('',views.index),
   path('about.html',views.about),
   path('Enquiry.html',views.Enquiry),
]
