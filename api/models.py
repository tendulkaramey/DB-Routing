from django.db import models
from django.utils.timezone import now

def default_json():
    return {}

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now, editable=False)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now, editable=False)

class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField(null=False)
    description = models.TextField(default='')
    stock = models.IntegerField(default=0)
    rating = models.FloatField(null=True)
    reviews = models.JSONField(default=default_json)
    additional_info = models.JSONField(default=default_json)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now, editable=False)
