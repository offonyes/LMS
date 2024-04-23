from django.urls import path
from universities_app.views import ProfileView, SubjectsView, AllSubjectsView, subject_detail, edit_subject
from accounts_app.views import redirecting_view

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', redirecting_view, name='edit_profile'),
    path('profile/edit/<int:user_id>/', edit_subject, name='edit_profile'),
    path('subjects/', SubjectsView.as_view(), name='subjects'),
    path('subject/<int:subject_id>/', subject_detail, name='subject'),
    path('subjects/edit/', edit_subject, name='edit'),
    path('all_subjects/', AllSubjectsView.as_view(), name='all_subjects'),
]
