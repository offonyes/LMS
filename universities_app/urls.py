from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from universities_app.views import (
    ProfileView,
    SubjectsView,
    AllSubjectsView,
    subject_detail,
    edit_subject,
)

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("subjects/", SubjectsView.as_view(), name="subjects"),
    path("subject/<int:subject_id>/", subject_detail, name="subject"),
    path("subjects/edit/", edit_subject, name="edit"),
    path("all_subjects/", AllSubjectsView.as_view(), name="all_subjects"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
