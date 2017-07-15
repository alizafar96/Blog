# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=300)
    text = models.TextField()
    creation_date = models.DateTimeField(timezone.now())
    publish_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.publish_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
