import django
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from universities_app.exceptions import DeadlineNotFitException


# Create your models here.


class Faculty(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Faculty name"), unique=True)

    class Meta:
        verbose_name = _("Faculty")
        verbose_name_plural = _("Faculties")

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Subject name"), unique=True)
    description = models.TextField(verbose_name=_("Description"))
    syllabus = models.FileField(verbose_name=_("Syllabus"), upload_to="syllabus/")
    # Many-to-Many
    faculties = models.ManyToManyField("Faculty", verbose_name=_("Faculties"))
    # One-to-One
    lecturer = models.OneToOneField(
        "Lecturer", on_delete=models.CASCADE, verbose_name=_("Lecturer")
    )
    # Many-to-Many
    student = models.ManyToManyField(
        "Student",
        verbose_name=_("Student"),
        limit_choices_to={"id__lte": 7},
        blank=True,
    )

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    # One-to-One
    user = models.OneToOneField(
        "accounts_app.CustomUser", on_delete=models.CASCADE, verbose_name=_("User")
    )
    first_name = models.CharField(
        max_length=200, verbose_name=_("Lecturer first name"), blank=True
    )
    last_name = models.CharField(
        max_length=200, verbose_name=_("Lecturer last name"), blank=True
    )

    class Meta:
        verbose_name = _("Lecturer")
        verbose_name_plural = _("Lecturers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    # One-to-One
    user = models.OneToOneField(
        "accounts_app.CustomUser", on_delete=models.CASCADE, verbose_name=_("User")
    )
    first_name = models.CharField(
        max_length=200, verbose_name=_("Student first name"), blank=True
    )
    last_name = models.CharField(
        max_length=200, verbose_name=_("Student last name"), blank=True
    )
    # ForeignKey
    faculty = models.ForeignKey(
        "Faculty", on_delete=models.CASCADE, verbose_name=_("Faculty")
    )

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Assignment(models.Model):
    lecturer = models.ForeignKey(
        "Lecturer", on_delete=models.CASCADE, verbose_name=_("Lecturer")
    )
    assignment_file = models.FileField(
        verbose_name=_("Assignment file"), upload_to="Assignments/"
    )
    description = models.TextField(verbose_name=_("Description"))
    deadline = models.DateTimeField(verbose_name=_("Deadline"))
    title = models.CharField(max_length=50, null=True, verbose_name=_("Title"))

    class Meta:
        verbose_name = _("Assignment")
        verbose_name_plural = _("Assignments")

    def __str__(self):
        return f"{self.lecturer} {self.title}"

    def is_in_time(self):
        return self.deadline > timezone.now()

    def get_available_responses(self):
        return AssignmentResponse.objects.filter(parent_assignment=self)


class AssignmentResponse(models.Model):
    parent_assignment = models.ForeignKey(
        "Assignment", on_delete=models.CASCADE, verbose_name=_("Parent assignment")
    )
    username = models.CharField(max_length=50, verbose_name=_("Username"))
    student_note = models.TextField(verbose_name=_("Student Note"))
    submit_date = models.DateTimeField(editable=False, default=django.utils.timezone.now(), verbose_name=_("Submit Date"))
    assignment_file = models.FileField(verbose_name=_("Assignment file"))

    def save(self, *args, **kwargs):
        upload_path = f"Assignments/{self.username}/"
        self.assignment_file.upload_to = upload_path
        super().save(*args, **kwargs)

    def submit(self):
        if self.parent_assignment.is_in_time():
            self.submit_date = timezone.now()
            self.save()
            return True
        raise DeadlineNotFitException

    class Meta:
        verbose_name = _("Assignment Response")
        verbose_name_plural = _("Assignment Responses")

    def __str__(self):
        return f"{self.parent_assignment.title} {self.username}"
