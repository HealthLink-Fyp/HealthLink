import time

from celery import shared_task

print("Start 1")


@shared_task
def send_mail_task(email: str, message: str):
    print("Start 2")
    time.sleep(10)
    print("Done!")
    # subject = "A new password to your HealthLink account has been requested"
    # send_mail(
    #     subject=subject,
    #     message=message,
    #     from_email=None,
    #     recipient_list=[email],
    #     fail_silently=False,
    # )

    # print("Mail Sent!")
