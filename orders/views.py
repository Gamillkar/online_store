from django.shortcuts import render
from .models import OrderItem, Order
from .forms import  OrderForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            total_sum = [item['total_price'] for item in cart]
            order = Order.objects.create(
                                first_name=form.cleaned_data['first_name'],
                                 last_name=form.cleaned_data['last_name'],
                                 email=form.cleaned_data['email'],
                                 address=form.cleaned_data['address'],
                                 postal_code=form.cleaned_data['postal_code'],
                                 city=form.cleaned_data['city'],
                                 total_sum = total_sum[0]
                                 )

            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'],
                                         )

                cart.clear()
                return render(request,
                    'orders/order/created.html',
                    {'order': order})

    else:
        form = OrderForm(request.POST)
        return render(request,
            'orders/order/create.html',
            {'cart': cart, 'form': form})


