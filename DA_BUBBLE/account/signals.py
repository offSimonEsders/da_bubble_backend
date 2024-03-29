from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import DA_Bubble_User

import os
from .tasks import get_file_mime_type
import time
from DA_BUBBLE.settings import BASE_DIR

@receiver(post_save, sender=DA_Bubble_User)
def rename_avatar_file(sender, instance, created, **kwargs):
    if created:
        os.rename(instance.avatar.path, 'media/avatars/' + instance.username + '_avatar' + get_file_mime_type(instance.avatar.name))
        instance.avatar.name = 'avatars/' + instance.username + '_avatar' + get_file_mime_type(instance.avatar.name)
        instance.save()
        
@receiver(post_delete, sender=DA_Bubble_User)
def remove_avatar_file(sender, instance, **kwargs):
    try:
        os.remove(instance.avatar.path)
    except:
        pass