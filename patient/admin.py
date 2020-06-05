from django.contrib import admin
from .models import patient


def change_condition(modeladmin, request, queryset):
    queryset.update(condition='g')


# Action description
change_condition.short_description = "Mark Selected Patient's Condition as Good"


# Data in list form
class patientA(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'gender', 'address', 'mobile', 'condition', 'status')

    list_filter = ('status', 'gender', 'name',)
    actions = [change_condition]

    # below mentioned code will not permit to update entry to status field by admin
    # exclude=('status',)


# Register your models here.
admin.site.register(patient, patientA)

# Changing the title of Django admin panel
admin.site.site_header = "ADMIN PANEL for Patient Record"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "WELCOME"
