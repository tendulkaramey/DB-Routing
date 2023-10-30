from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status as api_response_status
from api.models import *
from api.serializers import *
from django.core.paginator import Paginator

class ProductsByCategory(APIView):

    def get(self, request, format=None):

        category_id = request.GET.get('category')
        page = request.GET.get('page')

        category = Category.objects.get(id=category_id)
        subcategories = SubCategory.objects.filter(category=category)
        products = Product.objects.filter(sub_category__in=subcategories)

        paginator = Paginator(products, 10)
        products_page = paginator.get_page(page)      
        

        products = ProductSerializer(products_page, many=True)

        return JsonResponse({
            'success': True,
            'userMessage': '',
            'data': products.data,
        }, status = api_response_status.HTTP_200_OK)