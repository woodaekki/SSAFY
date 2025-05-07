# admin.py
from django.contrib import admin
from .models import DepositProducts, DepositOptions

admin.site.register(DepositProducts)
admin.site.register(DepositOptions)
