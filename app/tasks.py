from celery import shared_task
from django.core.mail import send_mail

@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y


@shared_task
def send_email_task(full_name, email, subject, message):
    
    response = send_mail(
        subject=subject,
        message=message,
        from_email=email,
        recipient_list=['admin@gmail.com'],
        fail_silently=False
    )

    return response
        