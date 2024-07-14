from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from materials.models import Course, Subscription
from users.models import User


@shared_task
def update_notification(course_pk):
    course = Course.objects.filter(pk=course_pk).first()
    users = User.objects.all()
    for user in users:
        subscription = Subscription.objects.filter(course=course_pk, user=user.pk).first()
        if subscription:
            send_mail(
                subject=f'Обновление курса "{course}"',
                message=f'Дорогой друг, курс "{course}", на который вы подписаны, обновился!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
