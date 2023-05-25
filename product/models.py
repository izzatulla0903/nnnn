from django.db import models



class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title