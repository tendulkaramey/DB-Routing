from api.views import ProductsByCategory
from django.urls import path

urlpatterns = [
    path('products-by-category', ProductsByCategory.as_view()),

]