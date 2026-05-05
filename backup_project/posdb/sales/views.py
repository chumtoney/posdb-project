# sales/views.py

from django.shortcuts import render, get_object_or_404
from .models import Product, Order
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem
from .forms import OrderItemForm


def product_list(request):
    """បង្ហាញផលិតផល active ទាំងអស់ តម្រៀប A–Z"""
    products = Product.objects.filter(is_active=True)
    return render(request, 'sales/product_list.html', {'products': products})


def product_detail(request, pk):
    """បង្ហាញព័ត៌មានលម្អិតសម្រាប់ផលិតផលតែមួយ។ Return 404 ប្រសិនបើរកមិនឃើញ"""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'sales/product_detail.html', {'product': product})


def order_list(request):
    """បង្ហាញការបញ្ជាទិញទាំងអស់ ថ្មីបំផុតមុន"""
    orders = Order.objects.all()
    return render(request, 'sales/order_list.html', {'orders': orders})
@login_required
def create_order(request):
    """Instantly create an open order and jump straight to the add-items page."""
    order = Order.objects.create(
        cashier=request.user,
        status='open',
    )
    return redirect('add_item', pk=order.pk)


@login_required
def add_item(request, pk):
    """
    Let the cashier add line items to an open order, then mark it paid.
    """
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        # "Mark as Paid" button
        if 'mark_paid' in request.POST:
            order.status = 'paid'
            order.save()
            return redirect('order_list')

        # Add a line item
        item_form = OrderItemForm(request.POST)
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.order      = order
            item.unit_price = item.product.price   # snapshot the current price
            item.save()
            return redirect('add_item', pk=order.pk)
    else:
        item_form = OrderItemForm()

    return render(request, 'sales/add_item.html', {
        'order':     order,
        'item_form': item_form,
        'items':     order.items.select_related('product'),
    })
