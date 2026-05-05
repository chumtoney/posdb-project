from django.urls import path
from . import views

urlpatterns = [
    # ផ្នែកផលិតផល
    path('products/', views.products_list, name='products_list'),
    path('products/<int:pk>/', views.products_detail, name='products_detail'),

    # ផ្នែកការបញ្ជាទិញ
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.create_order, name='create_order'),
    path('orders/<int:pk>/add-item/', views.add_item, name='add_item'),
]