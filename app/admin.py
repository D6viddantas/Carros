from django.contrib import admin
from app.models import Car,Brand


class CarAdmin(admin.ModelAdmin):
    list_display = ('model','brand','factory_year','model_year','value')
    search_fields = ('model',)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Car,CarAdmin)

