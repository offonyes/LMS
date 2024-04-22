from django.urls import path
from universities_app.views import ProfileView, SubjectsView, AllSubjectsView, subject_detail 
from accounts_app.views import redirecting_view

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('subjects/', SubjectsView.as_view(), name='subjects'),
    path('subject/<int:subject_id>/', subject_detail, name='subject'),
    path('all_subjects/', AllSubjectsView.as_view(), name='all_subjects'),
]
