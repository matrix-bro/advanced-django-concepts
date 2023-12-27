from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

from app.tasks import send_email_task

def index(request):
    return render(request, 'app/index.html')

@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    return render(request, 'app/dashboard.html')

def send_email(request):

    # Calling celery task
    response = send_email_task(request.POST['full_name'], request.POST['email'], request.POST['subject'], request.POST['message'])

    return redirect('index-page')