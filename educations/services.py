from datetime import timedelta

import django

from users.models import User


def search_user_old_online():
    date_now = django.utils.timezone.now()
    date_month = date_now - timedelta(days=30)
    list_user = User.objects.filter(last_login__lt=date_month)
    for user in list_user:
        user.is_active = False
        user.save()
    return None
