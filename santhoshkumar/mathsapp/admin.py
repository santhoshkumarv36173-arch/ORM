from django.contrib import admin
from .models import cars_DB,cars_DBAdmin
admin.site.register(cars_DB,cars_DBAdmin)