from django.contrib import admin
from universities_app.models import (
    Faculty,
    Subject,
    Lecturer,
    Student,
    Assignment,
    AssignmentResponse,
)
from accounts_app.models import CustomUser


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name")

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
    list_display = ("user", "first_name", "last_name")
    list_filter = ("faculty",)

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
    list_display = ("name", "description", "syllabus", "get_names")
    list_filter = ("faculties",)

    def get_names(self, obj):
        return obj.lecturer.first_name + " " + obj.lecturer.last_name

    get_names.short_description = "Lecturer"


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("lecturer", "subject", "description", "deadline")


@admin.register(AssignmentResponse)
class AssignmentResponseAdmin(admin.ModelAdmin):
    list_display = ("parent_assignment", "username", "submit_date")


admin.site.register(Faculty)
