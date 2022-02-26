from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Enquiryuser
# Register your models here.
# admin.site.register(Enquiryuser)

class EnquiryuserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Enquiryuser, EnquiryuserAdmin)

