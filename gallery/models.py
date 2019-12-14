# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
  types = models.CharField(max_length =100,null=True )
  def __str__(self):
    return self.types

class Location(models.Model):
  name = models.CharField(max_length =100,null=True)
  
  def __str__(self):
    return self.name

class Image(models.Model):
  Name = models.CharField(max_length = 40,null=True)
  Description = models.TextField()
  location = models.ForeignKey(Location,null=True)
  category = models.ForeignKey(Category,null=True)
  # Image = models.ImageField(upload_to='photos/')
