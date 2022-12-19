
from django.core.mail import send_mail

from django.conf import settings 


def send_forget_password_mail(email , token ):
    subject = 'Seu link de recuperação'
    message = f'Olá , clique no link para recuperar sua senha http://192.168.100.10:8000/change-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True
