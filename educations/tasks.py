from django.core.mail import send_mail
from config.celery import app
from config.settings import EMAIL_HOST_USER

from educations.models import Subscriptions, Course


@app.task
def send_email(course_id):
    subscriber_list = Subscriptions.objects.filter(course_id=course_id)
    subscriber_list_email = []
    course = Course.objects.get(id=course_id)
    subject = f"Обновление курса '{course}'"
    message = f"Курс '{course}' обновился, вы можете с ним ознакомиться."
    for subscriber in subscriber_list:
        subscriber_list_email.append(subscriber.user.email)
    send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        subscriber_list_email
    )
