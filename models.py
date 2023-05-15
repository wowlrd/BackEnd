from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    description = models.TextField(help_text='Description for this product', null=True)
    picture = models.ImageField(upload_to='media')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(help_text='Write here')
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, through='BasketItem')
    date_created = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return sum(item.get_price() for item in self.basketitem_set.all())


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def get_price(self):
        return self.product.price * self.quantity

    def save(self, *args, **kwargs):
        self.total_price = self.get_price()
        super().save(*args, **kwargs)
