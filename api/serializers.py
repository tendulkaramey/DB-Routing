from rest_framework import serializers
from api.models import *

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    sub_category = serializers.SerializerMethodField()

    def get_sub_category(self, product):
        subcategory = SubCategorySerializer(product.sub_category)
        return subcategory.data
    class Meta:
        model = Product
        fields = '__all__'