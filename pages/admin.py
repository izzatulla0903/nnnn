from django.contrib import admin
from pages.models import Car
from pages.models import Musician
from pages.models import Notebook


admin.site.register(Musician)
admin.site.register(Car)
admin.site.register(Notebook)