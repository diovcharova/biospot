from django.db import models


class Tag(models.Model):
    tags = models.ForeignKey('Product', on_delete=models.CASCADE)
    tag = models.CharField(max_length=15)


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    category = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
