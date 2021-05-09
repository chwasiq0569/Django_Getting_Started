from django.contrib import admin

# Register your models here.
from orm.models import Student


# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['stuid', 'stuname', 'stuemail', 'stuepass', 'comment']


# admin.site.register(Student, StudentAdmin)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['stuid', 'stuname', 'stuemail', 'stuepass', 'comment']
