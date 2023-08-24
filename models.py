from typing import Text
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    house_number = models.CharField(max_length=50)
    locality = models.CharField(max_length=500)
    landmark = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

    def __str__(self):
        name = str(self.name)
        phone_number = str(self.phone_number)
        house_number = str(self.house_number)
        locality = str(self.locality)
        id = str(self.id)
        return (f"({id}) {name}/{phone_number}, H.No: {house_number}, {locality}")


CATEGORY_CHOICES = (
    ('S', 'Shoes'),
    ('C', 'Crocs'),
    ('F', 'Flips'),
)



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    contact_for = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        id = str(self.id)
        name = str(self.name)
        email = str(self.email)
        contact_for = str(self.contact_for)

        return(f"{name}({email}): {contact_for}")


class Product(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    original_price = models.FloatField()
    price = models.FloatField()
    # unit = models.CharField(choices=UNIT, max_length=7)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_img = models.ImageField(upload_to='productimg')

    def __str__(self):
        title = str(self.title)
        price = str(self.price)
        id = str(self.id)
        return (f"ID: {id} -  {title} - Rs{price}")


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.price


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Canceled', 'Canceled'),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              default='Pending', max_length=50)

    @property
    def total_cost(self):
        return self.quantity * self.product.price
