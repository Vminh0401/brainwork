from django.contrib import admin

# Register your models here.

from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id_course', 'name_course', 'description', 'status', 'pl_course', 'objects_course', 'target', 'gv', 'content']

    search_fields = ['id_course', 'name_course', 'description', 'status', 'pl_course', 'objects_course', 'target', 'gv', 'content']
