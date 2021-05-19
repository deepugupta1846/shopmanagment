from django.db import models

# Create your models here.


class ShopManagment(models.Model):
    Item_Name = models.CharField(max_length=50)
    Company = models.CharField(max_length=50, default='')
    Type = models.CharField(max_length=50, default='')
    Rate = models.IntegerField(max_length=5)

    def __str__(self):
        return f"{self.Item_Name}-{self.Rate}"

gen = (
    ('male', 'Male'),
    ('female', 'Female')
)


#class AddCustomer(models.Model):
   # Customer_Name = models.CharField(max_length=50)
    #Gender = models.CharField(max_length=10, choices=gen)
    #Address = models.CharField(max_length=200)
    #Phone = models.CharField(max_length=12)
    #Item_Id = models.ForeignKey(ShopManagment)
