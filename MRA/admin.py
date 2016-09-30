from django.contrib import admin

# Register your models here.
from .models import Employee, Unit, Parts



class EmployeeAdmin(admin.ModelAdmin):
    list_display= ('first_name', 'last_name', 'title')
    list_filter = ['last_name']
    search_fields = ['last_name']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Unit)
admin.site.register(Parts)
