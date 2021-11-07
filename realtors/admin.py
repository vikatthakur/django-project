from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'hire_date', 'is_mvp', 'description',)
    list_editable = ('is_mvp', 'phone', )
    list_filter = ('id', 'name',)
    search_fields = ('id', 'name', 'email', 'address', )

admin.site.register(Realtor, RealtorAdmin)