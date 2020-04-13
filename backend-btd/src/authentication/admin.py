from django.contrib import admin
from .models import CustomUser, Brewery

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Brewery)