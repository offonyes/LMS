from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from universities_app.views import (
    ProfileView, SubjectsView, AllSubjectsView, edit_subject,
    SubjectDetailView, AssigmentsView, AssignmentCreateView, AssignmentResponseCreateView, 
    AssignmentResponseUpdateView, AssignmentDetailView, AttendanceView, create_attendance)

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('subjects/', SubjectsView.as_view(), name='subjects'),
    path('subject/<int:subject_id>/', SubjectDetailView.as_view(), name='subject'),
    path('subjects/edit/', edit_subject, name='edit'),
    path('all_subjects/', AllSubjectsView.as_view(), name='all_subjects'),
    path('assigments/', AssigmentsView.as_view(), name='assigments'),
    path('assigment/<int:assigment_id>/', AssignmentDetailView.as_view(), name='assigment'),
    path('assigment_response/new/<int:assigment_id>/', AssignmentResponseCreateView.as_view(), name='assigment_response_new'),
    path('assigment_response/edit/<int:assigment_id>/', AssignmentResponseUpdateView.as_view(), name='assigment_response_edit'),
    path('create_assigments/', AssignmentCreateView.as_view(), name='create_assigments'),
    path('attendances/', AttendanceView.as_view(), name='attendances'),
    path('attendances/new/', create_attendance, name='attendance_new'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
