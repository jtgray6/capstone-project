from django.contrib import admin
from .models import CustomUser, Brewery, Beer

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Brewery)
admin.site.register(Beer)