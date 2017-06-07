from django.db import models


class Item(models.Model):
    """
    Item Model
    """
    text = models.TextField(default='')
