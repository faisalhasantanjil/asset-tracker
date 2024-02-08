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
    path('assign-asset', views.assign_asset, name='assign_asset'),
    path('assign-assets', views.view_assigned_asset, name='view_assign_asset'),
    path('assign-assets/<str:pk>', views.assigned_asset_details, name='assign_asset_details'),
]
