from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrderForm

@login_required # បង្ខំឱ្យ Login សិនទើបចូលបាន
def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.staff = request.user # ភ្ជាប់ការលក់ទៅកាន់បុគ្គលិកដែលកំពុង Login
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'pos/order_form.html', {'form': form})