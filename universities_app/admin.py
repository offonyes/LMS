from django.contrib import admin
from .models import Faculty, Subject, Lecturer, Student, CustomUser
from django.db.models import Count


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')

    def save_model(self, request, obj, form, change):
        obj.first_name = obj.user.first_name
        obj.last_name = obj.user.last_name
        super().save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = CustomUser.objects.exclude(student__isnull=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')

    def save_model(self, request, obj, form, change):
        obj.first_name = obj.user.first_name
        obj.last_name = obj.user.last_name
        super().save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = CustomUser.objects.exclude(lecturer__isnull=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'syllabus', 'get_names')
    
    def get_names(self, obj):
        return obj.lecturer.first_name + ' ' + obj.lecturer.last_name
    
    get_names.short_description = 'Lecturer'


admin.site.register(Faculty)    
