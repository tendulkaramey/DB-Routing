from django.core.management.base import BaseCommand
import random
from datetime import datetime, timedelta
from faker import Faker
from api.models import *

categories = ['Fresh', 'Books', 'Sports', 'Electronics', 'Fashion']
subcategories = {
    'Fresh': ['Fruits & Vegetables', 'Dairy & Bread', 'Snacks', 'Instant Food'],
    'Books': ['Fiction', 'Children', 'Academic', 'Travel', 'History'],
    'Sports': ['Cricket', 'Football', 'Badminton', 'Running', 'Cycling', 'Accesories'],
    'Electronics': ['Mobiles', 'Laptops', 'Televisions', 'Cameras', 'Home Appliances'],
    'Fashion': ['Men Clothing', 'Women Clothing', 'Shoes', 'Accesories'],
}
fake = Faker()

class Command(BaseCommand):
    help = 'Custom management command description'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        SubCategory.objects.all().delete()
        Category.objects.all().delete()

        #code to add category and subcategory
        bulk_add_categories = []
        for category in categories:
            category_obj = Category(name=category)
            bulk_add_categories.append(category_obj)

        Category.objects.bulk_create(bulk_add_categories)

        category_objects = {}
        categories_objects = Category.objects.using('primary').all()
        for category in categories_objects:
            category_objects[category.name] = category

        bulk_add_sub_categories = []
        for category, subcategory_list in subcategories.items():
            category_object = category_objects[category]
            for sub_cat_name in subcategory_list:
                subcategory_obj = SubCategory(name=sub_cat_name, category=category_object)
                bulk_add_sub_categories.append(subcategory_obj)

        SubCategory.objects.bulk_create(bulk_add_sub_categories)
        subcategory_objects = {}
        subcategories_objects = SubCategory.objects.using('primary').all()
        for subcategory in subcategories_objects:
            subcategory_objects[subcategory.name] = subcategory

        print('now generating products.............')
        #generate fake data using faker.
        def generate_product():
            category_name = random.choice(categories)
            subcategory_name = random.choice(subcategories[category_name])
            
            product = {
                'sub_category': subcategory_name,
                'name': fake.word(),
                'price': round(random.uniform(1, 1000), 2),
                'description': fake.sentence(),
                'stock': random.randint(0, 100),
                'rating': round(random.uniform(1, 5), 2),
                'reviews': [{'author': fake.name(), 'comment': fake.paragraph(), 'rating': random.randint(1, 5)} for _ in range(random.randint(0, 5))],
                'additional_info': {
                    'brand': fake.company(),
                    'model': fake.word(),
                },
                'is_active': random.choice([True, False]),
                'created_at': (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%dT%H:%M:%S"),
            }
            
            return product
        bulk_add_products = []
        for i in range(0,300):
            product = generate_product()
            sub_category_obj = subcategory_objects[product['sub_category']]
            product_obj = Product(sub_category=sub_category_obj, name=product['name'], price=product['price'], description=product['description'], stock=product['stock'], rating=product['rating'], reviews={'reviews':product['reviews']}, additional_info=product['additional_info'], is_active=product['is_active'], created_at=product['created_at'])
            bulk_add_products.append(product_obj)

        Product.objects.bulk_create(bulk_add_products)
        self.stdout.write(self.style.SUCCESS('Successfully populated database.'))

