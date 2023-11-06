from django.conf import settings
from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import PostCategory, Post, Author
from django.utils import timezone
from datetime import datetime


def send_notifications(preview, pk, caption, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=caption,
        body=preview,
        from_email='NewsPortal50@yandex.ru',
        to=subscribers,
    )
    msg.attach_alternative(html_content, "text/html")

    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers_emails = []

        for cat in categories:
            subscribers = cat.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.caption, subscribers_emails)


@receiver(pre_save, sender=Author)
def check_for_saves(sender, instance, **kwargs):
    current_author = instance.author.id
    current_time = datetime.now(tz=timezone.utc)
    day = datetime(days=1)
    time = current_time - day

    for i in Post.objects.all().filter(author=current_author, published_date=time):
        if len(i) > 3:
            raise Exception("Простите, вы не можете публиковать более 3 постов в день.")
