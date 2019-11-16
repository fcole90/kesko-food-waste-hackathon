from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Article(models.Model):
    """
    Models available articles
    """
    name = models.CharField(max_length=200)
    serial_id = models.CharField(max_length=200)


class ArticlePurchase(models.Model):
    """
    Models users purchases.
    """
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField()
