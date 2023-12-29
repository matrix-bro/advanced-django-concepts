from django.urls import path
from app.views import index, send_email, dashboard, profile

urlpatterns = [
    path('', index, name='index-page'),
    path('dashboard/', dashboard, name='dashboard-page'),
    path('profile/', profile, name='profile-page'),
    path('send_email/', send_email, name='send-email'),
]
