# Ex02 Django ORM Web Application
## Date: 15.09.25

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import cars_DB,cars_DBAdmin
admin.site.register(cars_DB,cars_DBAdmin)

models.py

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

```


## OUTPUT
![alt text](<Screenshot 2025-09-14 235738.png>)



## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
