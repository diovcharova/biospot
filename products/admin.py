from django.contrib import admin
from .models import Product, Tag, Category, Producer


admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Producer)
