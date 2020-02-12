from django.conf.urls import url
from .views import all_products, products_skincare_and_beauty, products_bulk, products_cleaning_and_household, products_organic, products_supplements, products_raw_and_superfoods

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^skincare/$', products_skincare_and_beauty, name='skincare'),
    url(r'^bulk/$', products_bulk, name='bulk'),
    url(r'^cleaning/$', products_cleaning_and_household, name='cleaning'),
    url(r'^organic/$', products_organic, name='organic'),
    url(r'^supplements/$', products_supplements, name='supplements'),
    url(r'^raw/$', products_raw_and_superfoods, name='raw'),

]
