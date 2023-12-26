from django.shortcuts import render, redirect

from app.tasks import send_email_task

def index(request):
    return render(request, 'app/index.html')

def send_email(request):

    # Calling celery task
    response = send_email_task(request.POST['full_name'], request.POST['email'], request.POST['subject'], request.POST['message'])

    return redirect('index-page')