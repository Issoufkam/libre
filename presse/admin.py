from django.contrib import admin
from .models import Coursier, RechargeTransaction

# Register your models here.
admin.site.register(Coursier)
admin.site.register(RechargeTransaction)