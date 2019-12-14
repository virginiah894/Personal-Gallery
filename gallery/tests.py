# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from gallery.models import Image,Category,Location

# Create your tests here.
class CategoryTestClass(TestCase):

  def setUp(self):

    self.cat1 = Category(types='food')
  def test_instance(self):
    self.assertTrue(isinstance(self.cat1,Category))
class LocationTestClass(TestCase):
  def setUp(self):

    self.name = Location(name='kenya')
  def test_instance(self):
    self.assertTrue(isinstance(self.name,Location))
