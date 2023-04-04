from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("date", "status")
    ordering = ("first_name", )
    readonly_fields = ("status", )


admin.site.register(Form, FormAdmin)



