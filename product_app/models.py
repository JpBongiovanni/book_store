from django.db import models

class SaleItem(models.Model):
    title = models.CharField(max_length=255, default='null')
    isbn13 = models.CharField(max_length=255, default='null')
    isbn = models.CharField(max_length=255, default='null')
    image = models.CharField(max_length=255, default='null')
    id = models.CharField(max_length=255, primary_key=True)
    link = models.TextField()
    customer_rating = models.IntegerField(blank=True, null=True, default="null")
    
    