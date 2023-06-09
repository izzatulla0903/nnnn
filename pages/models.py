from distutils.command.upload import upload
from django.db import models

class Musician(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=40)

    def __str__(self): return f'{self.name}{self.last_name}'


class Car(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    year = models.CharField(max_length=30)
    probeg = models.PositiveIntegerField()
    condition = models.CharField(max_length=250)
    color = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self) -> str: return f'{self.title} - {self.price}'


class Notebook(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    processor = models.CharField(max_length=200)
    Videocarta = models.CharField(max_length=250)
    Pitanie = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')

    def __str__(self) -> str: return f'{self.title} - {self.price}'

    