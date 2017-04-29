# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import forms
# Create your models here.


class User(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    name = models.CharField(blank=False, null=False,max_length=30,default="")  # This field type is a guess.
    login = models.CharField(blank=False, null=False,max_length=30,default="")  # This field type is a guess.
    password = models.CharField(blank=False, null=False,max_length=30,default="")  # This field type is a guess.
    email = models.EmailField(max_length=254,null=False,blank=True)
    class Meta:
        managed = True
        db_table = 'User'
