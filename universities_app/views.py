from typing import Any
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.utils.decorators import method_decorator
from universities_app.models import Subject, Student, Assignment, AssignmentResponse, Attendance
from django.shortcuts import get_object_or_404, redirect, render
from universities_app.forms import LecturerForm, StudentForm, AssignmentForm, AssignmetResponseForm
from django.utils import timezone


@method_decorator(login_required(login_url='/'), name='dispatch')
class ProfileView(TemplateView):
    template_name = 'universities_app/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if hasattr(user, 'lecturer'):
            context['role'] = 'Lecturer'
        elif hasattr(user, 'student'):
            context['role'] = 'Student'
        return context


@method_decorator(login_required(login_url='/'), name='dispatch')
class SubjectsView(TemplateView):
    template_name = 'universities_app/my_subjects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if hasattr(user, 'lecturer'):
            context['subjects'] = Subject.objects.filter(lecturer=user.lecturer)
            context['subjects_count'] = context['subjects'].count()
            context['max_subjects'] = 1
            context['role'] = 'Lecturer'
        elif hasattr(user, 'student'):
            context['subjects'] = Subject.objects.filter(student=user.student)
            context['subjects_count'] = context['subjects'].count()
            context['max_subjects'] = 7
            context['role'] = 'Student'
        return context


@method_decorator(login_required(login_url='/'), name='dispatch')
class AllSubjectsView(ListView):
    template_name = 'universities_app/all_subjects.html'
    model = Subject
    context_object_name = 'subjects'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(login_required(login_url='/'), name='dispatch')
class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'universities_app/subject_id.html'
    context_object_name = 'subject'
    pk_url_kwarg = 'subject_id'


@login_required(login_url='/')
def edit_subject(request):
    if hasattr(request.user, 'lecturer'):
        subject_instance = Subject.objects.get(lecturer=request.user.lecturer)
        form = LecturerForm(instance=subject_instance)
    elif hasattr(request.user, 'student'):
        student_instance = Student.objects.get(user=request.user)
        subjects = student_instance.subject_set.all()
        form = StudentForm(instance=student_instance, initial={'subjects': subjects}, user=request.user)

    if request.method == 'POST':
        if hasattr(request.user, 'lecturer'):
            form = LecturerForm(request.POST, instance=subject_instance)
            if form.is_valid():
                form.save()
                return redirect('subjects')
        else:
            form = StudentForm(request.POST, instance=student_instance, user=request.user)
            if form.is_valid():
                form.save()
                student_instance.subject_set.set(form.cleaned_data['subjects'])
                return redirect('subjects')

    return render(request, 'accounts_app/edit_subject.html', {'form': form})


@method_decorator(login_required(login_url='/'), name='dispatch')
class AssigmentsView(ListView):
    template_name = 'universities_app/assigments.html'
    model = Assignment
    context_object_name = 'assignments'

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'student'):
            subjects = user.student.subject_set.all()
            queryset = Assignment.objects.filter(lecturer__subject__in=subjects).order_by('-deadline').distinct()
        elif hasattr(user, 'lecturer'):
            queryset = Assignment.objects.filter(lecturer=user.lecturer).order_by('-deadline')
        return queryset

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        if hasattr(user, 'lecturer'):
            context['role'] = 'Lecturer'
            context['max_students'] = Student.objects.filter(subject=user.lecturer.subject).count()
        elif hasattr(user, 'student'):
            context['role'] = 'Student'

            assignments = context['assignments']
            assignment_responses_exist = {}
            for assignment in assignments:
                if assignment.assignmentresponse_set.filter(student=user.student).exists():
                    assignment_responses_exist[assignment.id] = assignment.assignmentresponse_set.filter(
                        student=user.student).exists()
            context['assignment_responses_exist'] = assignment_responses_exist
        return context


class AssignmentCreateView(CreateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = 'universities_app/lecturer/new_assignments.html'
    success_url = reverse_lazy('assigments')

    def form_valid(self, form):
        form.instance.lecturer = self.request.user.lecturer
        return super().form_valid(form)


class AssignmentDetailView(ListView):
    model = Assignment
    template_name = 'universities_app/lecturer/assigment_detail.html'
    pk_url_kwarg = 'assigment_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Assignment.objects.filter(pk=self.kwargs['assigment_id'])
        context['results'] = AssignmentResponse.objects.filter(parent_assignment__in=queryset)
        return context


class AssignmentResponseCreateView(CreateView):
    model = AssignmentResponse
    form_class = AssignmetResponseForm
    pk_url_kwarg = 'assigment_id'
    template_name = 'accounts_app/assignment.html'
    success_url = reverse_lazy('assigments')

    def form_valid(self, form):
        form.instance.student = self.request.user.student
        form.instance.submit_date = timezone.now()
        form.instance.parent_assignment = Assignment.objects.get(pk=self.kwargs['assigment_id'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Assignment"
        context['assigment'] = Assignment.objects.get(pk=self.kwargs['assigment_id'])
        return context


class AssignmentResponseUpdateView(UpdateView):
    model = AssignmentResponse
    form_class = AssignmetResponseForm
    pk_url_kwarg = 'assigment_id'
    template_name = 'accounts_app/assignment.html'
    success_url = reverse_lazy('assigments')

    def form_valid(self, form):
        form.instance.student = self.request.user.student
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit assignment"
        context['assigment'] = Assignment.objects.get(pk=self.kwargs['assigment_id'])
        return context


class AttendanceView(ListView):
    model = Attendance
    template_name = 'universities_app/lecturer/attendances.html'
    context_object_name = 'attendance_records'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['dates'] = Attendance.objects.dates('date', 'day')
        context['selected_date'] = self.get_selected_date()
        context['subject'] = Subject.objects.filter(lecturer=self.request.user.lecturer).first()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.GET.get('date')
        if date:
            queryset = queryset.filter(date=date)

        return queryset

    def get_selected_date(self):
        try:
            return self.request.GET.get('date')
        except TypeError:
            return None


def create_attendance(request):
    subject_id = request.user.lecturer.subject.id
    subject = get_object_or_404(Subject, id=subject_id)

    if request.method == 'POST':
        student_ids = request.POST.getlist('students')
        attended_student_ids = request.POST.getlist('attendance')
        for student_id in student_ids:
            attended = student_id in attended_student_ids
            student = get_object_or_404(Student, id=student_id)
            attendance, created = Attendance.objects.get_or_create(
                student=student,
                subject=subject,
                date=timezone.now(),
            )
            attendance.attended = attended
            attendance.save()

        return redirect('attendances')

    else:
        students = Student.objects.filter(subject=subject)
        return render(request, 'universities_app/lecturer/new_attendances.html',
                      {'students': students, 'subject': subject})
