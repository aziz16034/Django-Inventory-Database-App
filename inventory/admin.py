from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Laptop, Mobile, phone)

class ViewAdmin(admin.ModelAdmin):
    pass


