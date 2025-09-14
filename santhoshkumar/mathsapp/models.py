from django.db import models
from django.contrib import admin

class cars_DB(models.Model):
    brand_Name = models.CharField(max_length=10)
    modelno = models.IntegerField(primary_key=True)
    type_of_car = models.CharField(max_length=15)
    manufacture_dob = models.DateField()
    milage = models.FloatField()

class cars_DBAdmin(admin.ModelAdmin):
    list_display = ["brand_Name", "modelno", "type_of_car", "manufacture_dob", "milage"]
