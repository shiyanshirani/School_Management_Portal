from django.contrib import admin
from .models import Student, Teacher, Batch
# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Batch)