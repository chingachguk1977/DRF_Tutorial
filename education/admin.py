from django.contrib import admin
from .models import School, SClass, Student


# Register your models here.
admin.site.register(School)
admin.site.register(SClass)
admin.site.register(Student)
