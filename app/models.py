# Importing Required Libraries
from django.db import models
from django.contrib.auth.models import User


class GooglePlayModel(models.Model):
    """ Model to Store Google App Store App's Details """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="googleplay", null=True)
    name = models.CharField(max_length=30)
    app_name = models.CharField(max_length=40)
    image = models.CharField(max_length=200)
    developer = models.CharField(max_length=20)
    description = models.CharField(max_length=203)
    downloads = models.CharField(max_length=30)
    reviews = models.CharField(max_length=30)
    ratings = models.CharField(max_length=20)

    def __str__(self):
        return f"Created {self.app_name}"


class AppleAppModel(models.Model):
    """ Model to Store Apple App Store App's Details """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="appleapp", null=True)
    app_name = models.CharField(max_length=40)
    image = models.CharField(max_length=200)
    developer = models.CharField(max_length=20)
    description = models.CharField(max_length=203)
    reviews = models.CharField(max_length=30)
    ratings = models.CharField(max_length=20)

    def __str__(self):
        return f"Created {self.app_name}"


class Keyword(models.Model):
    """ Model to Store Url's Keywords """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="keywords", null=True)
    url = models.CharField(max_length=200)
    keyword = models.CharField(max_length=1000)
    rec_keyword = models.CharField(max_length=1000)

    def __str__(self):
        return self.keyword
