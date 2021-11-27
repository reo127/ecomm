from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default='0')
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    images = models.ImageField(upload_to="core/images", default="")

    def __str__(self):
        return self.product_name

class Orders(models.Model):
    product_sno = models.IntegerField(default=0)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=40)
    address = models.CharField(max_length=60)
    landMark = models.CharField(max_length=30)
    opitonlAddress = models.CharField(max_length=60)
    state = models.CharField(max_length=20)
    zip = models.CharField(max_length=10)
    payment = models.CharField(max_length=15)

    def __str__(self):
        return f'Product no {self.product_sno} on {self.address} and phone {self.phone}'


class Cart(models.Model):
    originalId = models.IntegerField(null=False)
    product_name = models.CharField(max_length=30)
    price = models.IntegerField(default='0')
    belongsTo = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Product no {self.originalId}, name is {self.product_name} and price {self.price} belongs to {self.belongsTo}'

    