from django.contrib import admin

# Register your models here.
from index import models
admin.site.register(models.User)
admin.site.register(models.Employee)
