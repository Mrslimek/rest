from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Sun


@receiver(post_save, sender=Sun)
def sun_saved(sender, instance, created, **kwargs):
    
    if created:
        print(f'Создан новый объект {instance.name}')
    else:
        print(f'Объект обновлен: {instance.name}')