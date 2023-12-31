from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status as api_response_status
from api.models import *
from api.serializers import *
from django.core.paginator import Paginator
from django.db.models import Prefetch

class ProductsByCategory(APIView):

    def get(self, request, format=None):

        category_id = request.GET.get('category')
        page = request.GET.get('page')

        if category_id is None:
            return JsonResponse({
                'success': False,
                'userMessage': 'category id missing.',
            }, status = api_response_status.HTTP_400_BAD_REQUEST)
        
        page = 1 if page is None else page

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return JsonResponse({
                'success': False,
                'userMessage': 'Not Found',
            }, status = api_response_status.HTTP_404_NOT_FOUND)

        subcategories = SubCategory.objects.filter(category=category)
        subcategories_prefetch = Prefetch('sub_category', queryset=subcategories)
        products = Product.objects.filter(sub_category__in=subcategories).prefetch_related(subcategories_prefetch).order_by('id') #to get uniform paginated results.

        paginator = Paginator(products, 10)
        products_page = paginator.get_page(page)      
        
        products = ProductSerializer(products_page, many=True)

        return JsonResponse({
            'success': True,
            'userMessage': '',
            'data': products.data,
        }, status = api_response_status.HTTP_200_OK)