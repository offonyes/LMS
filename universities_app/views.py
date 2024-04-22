from typing import Any
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from universities_app.models import Subject, Student
from django.shortcuts import render, get_object_or_404

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
            context['max_subjects'] = '∞'
            context['role'] = 'Lecturer'
        elif hasattr(user, 'student'):
            context['subjects'] = Student.objects.get(user=user).subjects.all()
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
        # context['role'] = self.request.user.role
        print(context)
        return context
    
    
def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'universities_app/subject_id.html', {'subject': subject})