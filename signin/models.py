# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class BookUser(models.Model):
    user1 = models.OneToOneField(User)
    email_id = models.EmailField(max_length = 50)
    phone_number = models.IntegerField(default = 0)
    address = models.TextField(max_length=100)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = BookUser.objects.create(user = kwargs['instance'])

post_save.connect(create_profile, sender=User)
