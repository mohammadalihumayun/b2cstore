from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Homepage
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})


# Product detail (THIS is missing in your case)
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})


# Add to cart
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('cart_view')


#  Cart view
def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for product_id, qty in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * qty
        total += subtotal

        items.append({
            'product': product,
            'qty': qty,
            'subtotal': subtotal
        })

    return render(request, 'store/cart.html', {
        'items': items,
        'total': total
    })

# check out
def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('product_list')

    items = []
    total = 0

    for product_id, qty in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * qty
        total += subtotal

        items.append({
            'product': product,
            'qty': qty,
            'subtotal': subtotal
        })

    return render(request, 'store/checkout.html', {
        'items': items,
        'total': total
    })