from django.urls import path, include
from django.contrib.auth.views import LogoutView

from apps.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('accounts/', include('allauth.urls')),
]
