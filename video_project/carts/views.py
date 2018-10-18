from __future__ import unicode_literals
from django.shortcuts import render, redirect   
from .models import Cart   
from products.models import Product
def cart_home(request): 
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    ## cart_id = request.session.get("cart_id", None) 
    ## qs = Cart.objects.filter(id = cart_id)
    ## if qs.count() ==1:
    ##     cart_obj = qs.first()
    ##     if request.user.is_authenticated() and cart_obj.user is None:
    ##         cart_obj.user = request.user
    ##         cart_obj.save() 
    ## else:
    ##     cart_obj = Cart.objects.new(user=request.user)
    ##     request.session['cart_id'] = cart_obj.id
    ##     print(request.session.get("cart_id"))
            
    # del request.session['cart_id'] #delete cart id form session        
    # print(request.session)
    # print(dir(request.session))
    # request.session.session_key(300)
    # key = request.session.session_key
    # request.session['first_name'] = 'Justin'

    # request.session['cart_id'] = 12 #set
    # request.session['user'] = request.user.username

    return render (request, "carts/home.html",{} )


def cart_update(request):
    product_id = 1
    product_obj = Product.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_obj  in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj) 
    
    # return redirect(product_obj.get_absolute_url()) 
    return redirect('cart:home')



