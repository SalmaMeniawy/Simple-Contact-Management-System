from django.contrib import admin
from .models import Contact
# Register your models here.
@admin.register(Contact)
class CintactAdmin(admin.ModelAdmin):
    list_display = ['name','address','phone','mobile']
    ordering = ('name',)
    search_fields = ['name']
# admin.site.register(Contact)
