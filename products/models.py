from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=40, default="")

    def __str__(self):
        return self.category


class Producer(models.Model):
    producer = models.CharField(max_length=40, default="")

    def __str__(self):
        return self.producer


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    package = models.CharField(max_length=45, default='', blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    producer = models.ForeignKey(Producer, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    code_internal = models.IntegerField(null=True)

    def __str__(self):
        return self.name
