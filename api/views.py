from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status as api_response_status
from api.models import *
from api.serializers import *

class ProductsByCategory(APIView):

    def get(self, request, id, format=None):

        category = Category.objects.get(id=id)
        subcategories = SubCategory.objects.filter(category=category)      
        products = Product.objects.filter(sub_category__in=subcategories)

        products = ProductSerializer(products, many=True)

        return JsonResponse({
            'success': True,
            'userMessage': '',
            'data': products.data,
        }, status = api_response_status.HTTP_200_OK)