from django.contrib import admin
from .models import Shop,Category
# Register your models here.

admin.site.register(Category)

@admin.register(Shop)


class ShopAdmin(admin.ModelAdmin):
    list_display = ['id','name','author',]
    list_filter = ['name','author']
    search_fields = ['name','body','author']
