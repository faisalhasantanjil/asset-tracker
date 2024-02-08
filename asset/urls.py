from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.tempo, name='tempo'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('add-employee/', views.addemployee, name='addemployee'),
    path('edit-employee/', views.addemployee, name='editemployee'),
    path('view-employee/', views.employeelist, name='employeelist'),
    path('view-employee/<str:pk>', views.employeedetails, name='employeedetails'),
]
