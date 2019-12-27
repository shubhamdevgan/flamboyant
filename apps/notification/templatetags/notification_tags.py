
from django import template

from apps.notification.models import notification

register = template.Library()

@register.filter
def has_unread_notif(user):
    notifications = notification.objects.filter(user__Username__username=user, status=False)
    print(notifications)
    if notifications.exists():
        return True
    return False