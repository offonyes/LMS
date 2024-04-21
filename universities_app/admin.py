from django.contrib import admin
from lms_app.models import Faculty, Student, Subject, Lecturer, PlainCustomUser


class FacultyAdmin(admin.ModelAdmin):
    list_display = ("name",)


class LecturerAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "surname")


class StudentAdmin(admin.ModelAdmin):
    def display_subjects(self, obj):
        return ", ".join([subject.name for subject in obj.subjects.all()])

    list_display = ("user", "name", "surname", "display_subjects", "faculty")


class UserAdmin(admin.ModelAdmin):
    list_display = ("username",)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "syllabus", "display_faculties", "display_students", "lecturer")

    def display_faculties(self, obj):
        return ", ".join([faculty.name for faculty in obj.faculties.all()])

    def display_students(self, obj):
        return ", ".join([student.name for student in obj.students.all()])


admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(PlainCustomUser, UserAdmin)
