from django.contrib import admin
from .models import Product  # ហៅ Model Product មកប្រើ

# ចុះឈ្មោះ Product ទៅកាន់ Admin Site
admin.site.register(Product)