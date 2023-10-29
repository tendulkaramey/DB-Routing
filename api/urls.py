from api.views import ProductsByCategory
from django.urls import path

urlpatterns = [
    path('products-by-category/<int:id>', ProductsByCategory.as_view()),

]