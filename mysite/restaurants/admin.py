from django.contrib import admin
from restaurants.models import Restaurant, Food 

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Food)