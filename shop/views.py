from urllib.parse import urlencode
from django.core.paginator import Paginator
from .models import Category
from django.shortcuts import render,  get_object_or_404
from shop.models import Product
from cart.forms import CartAddProductForm


def product_detail(request, id, slug,category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)

    product = get_object_or_404(Product,
                             id=id,
                             slug=slug,
                             available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
        'shop/product/detail.html',
        {'product': product,
        'cart_product_form': cart_product_form,
         'category': category,
         'categories': categories,
         })


def product_list(request, category_slug=None):
    form = CartAddProductForm(request.POST)

    # cd = form.cleaned_data
    # quantity = cd['quantity'],
    # override_quantity = cd['override']
    # print(quantity, override_quantity)
    if request.method == 'POST':
        form = CartAddProductForm(request.POST)


    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    cart_product_form = CartAddProductForm()
    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(products, 3)

    page_obj = paginator.get_page(current_page)
    prev_page, next_page = None, None
    if page_obj.has_previous():
        prev_page = urlencode({'page': current_page - 1})
        prev_page = f'?{prev_page}'
    if page_obj.has_next():
        next_page = urlencode({'page': current_page + 1})
        next_page = f'?{next_page}'
    context = {
        'form':form,
        'category': category,
         'categories': categories,
         'products': page_obj,
        'current_page': current_page,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
    }
    return render(request,
                  'shop/product/list.html',
                    context=context
                  )


