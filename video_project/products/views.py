# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Product
# from django.views import ListView
from django.views.generic import ListView, DetailView

from django.http import  Http404


class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.features()

class ProductFeaturedDetailView(DetailView):
    template_name = 'products/featured-detail.html'
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.features()

class ProductListView(ListView):
    # first way
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    
    # 2 way        
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render (request, "products/list.html", context)

def product_detail_view(request, pk = None, *args, **kwargs):
    # print(kwargs)
    # first way --------
    # data = Product.objects.filter(pk=pk)

    # 2 way-----------
    # data = get_object_or_404(Product, pk=pk)

    # 3 way with manager------------
    data = Product.objects.get_by_id(pk)
    if data is None:
        raise Http404('Product Does Not Exist dear :)')
    # 4 way-----------
    # try: 
    #     data = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('No products exists')
    #     raise Http404('Product Does Not Exist dear :)')
    # except:
    #     print('Huh?')

    # 5 way-------------
    # qs = Product.objects.filter(id=pk) # len(qs) is also use
    # if qs.exists() and qs.count() == 1:
    #     data = qs.first()
    # else :
    #     raise Http404('Product Does Not Exist dear, Not right url')

    context = {
        'object' : data,
        'abc': 'function base view'
    }
    
    return render(request, "products/detail.html", context)



class productDetailView(DetailView):
    # first way-----------------
    # queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(productDetailView, self).get_context_data(*args, **kwargs)
        context['abc'] = 'Class base view'
        
        return context
    def get_context_data(self, *args, **kwargs):
        context = super(productDetailView, self).get_context_data(*args, **kwargs)
        context['abc'] = 'Class base view'
        print(context)
        return context

    # 2 way------------------
    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404('Product Does Not Exist dear :)')
    #     return instance

    # 3 way------------------
    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk = pk)


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all() 
    template_name = "products/detail.html"
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     print(request)
    #     pk = self.kwargs.get('slug')
    #     return Product.objects.filter(slug = slug)

