from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class CompanyInformation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, unique=True)

    def __str__(self):
        return self.name

class EmployeeInformation (models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default='Employee Name')
    designation = models.CharField(max_length=50, null=True, blank=True)
    email= models.EmailField(unique=True, blank= True, null= True)
    company = models.ForeignKey(
        CompanyInformation, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name

class AssetTrack (models.Model):
    CATEGORY = [
        ('Laptop', 'Laptop'),
        ('Tablet', 'Tablet'),
        ('Phone', 'Phone'),
        ('Computer Accessories', 'Computer Accessories'),
        ('Stationery', 'Stationery'),
        ('Printing Accessories', 'Printing Accessories'),
        ('Safety Accessories', 'Safety Accessories'),
        ('Others', 'Others')
    ]
    
    CONDITION = [
        ('No Damage', 'No Damage'),
        ('Partially Damage', 'Partially Damage'),
        ('Damage', 'Damage'),
        ('Others', 'Others')
    ]
    STATUS = [
        ('Pending', 'Pending'),
        ('Returned', 'Returned'),
        ('No Return', 'No Return'),
        
    ]
    
    name = models.CharField(max_length=100, blank=True, null=True, default='')
    category = models.CharField(max_length=20, null=True, blank=True, choices=CATEGORY)
    company = models.ForeignKey(
        CompanyInformation, on_delete=models.CASCADE, blank=True, null=True)
    employee=models.ForeignKey(
        EmployeeInformation, on_delete=models.CASCADE, blank=True, null=True)
    assign_date = models.DateTimeField(blank=True, null=True)
    assign_time = models.TimeField(
        blank=True, null=True)
    initial_condition = models.CharField(max_length=20, null=True, blank=True, choices=CONDITION)
    initial_condition_log = models.CharField(max_length=500, blank=True, null=True, default='')
    return_date = models.DateTimeField(blank=True, null=True)
    return_time = models.TimeField(
        blank=True, null=True)
    return_condition = models.CharField(max_length=20, null=True, blank=True, choices=CONDITION)
    return_condition_log = models.CharField(max_length=500, blank=True, null=True, default='')
    status = models.CharField(max_length=20, null=True, blank=True, choices=STATUS, default='Pending')

    def __str__(self):
        return self.name
    
    