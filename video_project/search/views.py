# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from django.db.models import Q
class SearchProductView(ListView):
    # first way
    # queryset = Product.objects.all()
    # template_name = "products/list.html"
    template_name = "search/view.html"
     
    def get_context_data(self, *args, **kwargs):
        print ('+++++++++++++++++++++++++++++++++++++++')
        print(args)
        print ('+++++++++++++++++++++++++++++++++++++++')
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('search')
        return context
    
    # 2 way        
    def get_queryset(self, *args, **kwargs):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        request = self.request
        # request.GET['search'] it will print search but if search will not come in url then it will genrate error
        # request.GET is python dict and get is help to find key value
        # it will not genrate error if search does not exits

        # you can give default value like this request.GET.get('key', None) #none is default value if key does not exists
        query = request.GET.get('search') 
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        if query is not None:
            lookups = Q(title__icontains=query) | Q (description__icontains=query)
            a =  Product.objects.filter(lookups ).distinct()
            a =  Product.objects.searchq( query)
        else:
            a = Product.objects.all()
        return a

        '''
            __icontains = field contains this 
            __iexact = fields is exactly this
        '''
 