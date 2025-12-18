import random 
import string
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from smtplib import SMTPException

def generate_otp():
    return ''.join(random.choices(string.digits, k = 6))

def generate_reset_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k = 64))

def send_email(subject, message, to_email):
    print("In send mail function from utils file ")
    send_mail(
        subject,
        message,
        'twomindscreate17@gmail.com',
        [to_email],
        fail_silently=False    
        )
    
def send_email(subject, template_name, context, to_email):
    """
    Send HTML email using templates.
    """
    html_content = render_to_string(f'emails/{template_name}.html', context)
    email = EmailMessage(
        subject=subject,
        body=html_content,
        from_email=settings.EMAIL_HOST_USER,
        to=[to_email],
    )
    email.content_subtype = 'html'  # Set to HTML
    email.send()