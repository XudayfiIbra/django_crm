from django.contrib import admin
from . models import Record

class RecordAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'state', 'zipcode', 'created_at')


admin.site.register(Record, RecordAdmin)
