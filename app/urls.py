from django.urls import path
from app.views import index, send_email

urlpatterns = [
    path('', index, name='index-page'),
    path('send_email/', send_email, name='send-email'),
]
