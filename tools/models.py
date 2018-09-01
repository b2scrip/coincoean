from django.db import models

class Address(models.Model):
    code = models.CharField(max_length=500)
