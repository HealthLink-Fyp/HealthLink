# from celery import shared_task
# from django.core.mail import send_mail


# @shared_task
# def send_mail_task(email: str, message: str):
#     subject = "A new password to your HealthLink account has been requested"
#     send_mail(
#         subject=subject,
#         message=message,
#         from_email=None,
#         recipient_list=[email],
#         fail_silently=False,
#     )
