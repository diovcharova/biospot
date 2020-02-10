from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=30)

    def __str__(self):
        return self.tag


class Category(models.Model):
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category


class Producer(models.Model):
    producer = models.CharField(max_length=40)

    def __str__(self):
        return self.producer


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    categories = models.ManyToManyField(Category, blank=True, symmetrical=False)
    tags = models.ManyToManyField(Tag, blank=True)
    description = models.TextField()
    package = models.CharField(max_length=45,default='')
    producer = models.ManyToManyField(Producer, blank=True, symmetrical=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    code_internal = models.IntegerField(null=True)

    def __str__(self):
        return self.name
