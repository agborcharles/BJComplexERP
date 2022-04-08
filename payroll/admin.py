from django.contrib import admin
from . models import *

from import_export.admin import ImportExportModelAdmin

from django.db import models


class EmployeeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'get_full_name',]

class SubDepartmentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name',]


class RoleAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name',]

class SalariesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'employee', 'payment_type', 'payment_means', 'total_earnings', 'total_deductions',
                    'total_expected_amount_to_paid', 'total_amount_paid', 'arrears' ]


admin.site.register(SubDepartment, SubDepartmentAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Salaries, SalariesAdmin)
