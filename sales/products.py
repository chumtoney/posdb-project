# ── Run these lines inside: python manage.py shell ──

from sales.models import Products, Order, OrderItem

# ── 1. បង្កើតផលិតផល ──────────────────────────────────────────
coffee = Product.objects.create(
    name='កាហ្វេ Espresso',
    category='food',
    price=1.50,
    stock=100,
    barcode='FOOD-001',
)
sandwich = Product.objects.create(
    name='នំប៉័ង Club',
    category='food',
    price=3.99,
    stock=20,
    barcode='FOOD-002',
)
headphones = Product.objects.create(
    name='កាស Wireless',
    category='electronics',
    price=49.99,
    stock=15,
    barcode='ELEC-001',
)
charger = Product.objects.create(
    name='ខ្សែសាក USB-C',
    category='electronics',
    price=9.99,
    stock=4,      # ស្តុកទាប!
    barcode='ELEC-002',
)

print("ផលិតផលបានបង្កើត!")

# ── 2. បង្កើតការបញ្ជាទិញជាមួយ Items ──────────────────────────
order1 = Order.objects.create(cashier='សុភា', status='paid')

OrderItem.objects.create(
    order=order1,
    product=coffee,
    quantity=2,
    unit_price=coffee.price,
)
OrderItem.objects.create(
    order=order1,
    product=sandwich,
    quantity=1,
    unit_price=sandwich.price,
)

print(f"សរុបការបញ្ជាទិញ: ${order1.total:.2f}")   # គួរតែ print $6.99

# ── 3. ឧទាហរណ៍ Query ──────────────────────────────────────────

# ផលិតផលទាំងអស់ តម្រៀប A-Z
all_products = Product.objects.all()
print(f"ផលិតផលសរុប: {all_products.count()}")

# តែទំនិញ food
food_items = Product.objects.filter(category='food')
for p in food_items:
    print(p)

# ការព្រមានស្តុកទាប: ផលិតផលដែលមាន 5 ឬតិចជាងនេះ
low_stock = Product.objects.filter(stock__lte=5)
print("\n⚠️  ទំនិញស្តុកទាប:")
for p in low_stock:
    print(f"  {p.name}: {p.stock} នៅសល់")

# ផលិតផលតម្លៃលើសពី $10
expensive = Product.objects.filter(price__gt=10).order_by('-price')
for p in expensive:
    print(f"{p.name}: ${p.price}")

# ── 4. ធ្វើបច្ចុប្បន្នភាពស្តុក ────────────────────────────────
charger = Product.objects.get(barcode='ELEC-002')
charger.stock += 50    # ទំនិញផ្គត់ផ្គង់មកដល់ហើយ
charger.save()
print(f"ស្តុកបានធ្វើបច្ចុប្បន្នភាព {charger.name}: {charger.stock}")

# ── 5. Items ទាំងអស់នៅក្នុងការបញ្ជាទិញ #1 ────────────────────
for item in order1.items.all():
    print(f"  {item}  →  subtotal: ${item.subtotal:.2f}")