from django.urls import path
from accounts_app.views import login_register, redirecting_view

urlpatterns = [
    path('', login_register, name='reg'),
    path('home/', redirecting_view, name='home'),
]
