# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import random
import os
# Create your models here.

def get_filename_ext(filename):
	base_name = os.path.basename(filename)
	name, ext = os.path.splitext(base_name)
	return name, ext



def upload_image_path(instance, filename):
	print(instance)
	print(filename)
	new_filename = random.randint(1,344534534)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename = new_filename, ext = ext)
	# if you are using python3.6
	# final_filename = f'{new_filename}{ext}'
	return 'products/{new_filename}/{final_filename}'. format(
															new_filename=new_filename, 
															final_filename=final_filename
														)
class ProductQuerySet(models.query.QuerySet):
	def featured(self):
		return self.filter(featured = True)

	def active(self):
		return self.filter(active = True)

class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model , using = self._db)

	def all():
		return self.get_queryset().active() 
	def features(self):
		# return self.get_queryset().filter(featured = True)
		return self.get_queryset().featured()

	def get_by_id(self, id):
		qs = self.get_queryset().filter(id=id) #Product.objects == self.get_queryset()

		if qs.count() == 1: 
			return qs.first()
		return None



class Product(models.Model):
    title           = models.CharField(max_length = 120)
    slug			= models.SlugField(blank = True, null = True , default = 'abc')
    description     = models.TextField()
    price 			= models.DecimalField(decimal_places=2, max_digits=20, default = 49.99) #null = True
	# it will store any file fileField
	# image			= models.FileField(upload_to = upload_image_path, null =True, blank = True) 
    # null mean no need to add in db  any value, Blank means no require in django
    # Install Pillow
    image			= models.ImageField(upload_to = upload_image_path, null =True, blank = True) 
    featured 		= models.BooleanField(default = False)
    active 			= models.BooleanField(default = True)


    objects = ProductManager()

    def __str__(self):
    	return self.title

    def __unicode__(self):
    	return self.title

    
