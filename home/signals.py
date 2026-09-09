from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Students


@receiver(post_save, sender=Students)
def student_created(sender, instance, created, **kwargs):

    if created:
        print("New student created!")