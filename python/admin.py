from django.contrib import admin
from .models import pythonmodel
# Register your models here.


class pythonadmin(admin.ModelAdmin):
    list_display = ['student_id','first_name','last_name','date_of_birth','gender','email',
                    'phone_number','high_school_name','graduation_year','major','is_admitted','admission_date']

admin.site.register(pythonmodel,pythonadmin)