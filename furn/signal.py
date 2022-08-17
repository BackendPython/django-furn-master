from django.db.models.signals import post_save
from .models import MyUser, Profile
from django.dispatch import receiver

@receiver(post_save, sender=MyUser)
def create_profile(sender, instace, created, **kwargs):
    if created:
        Profile.objects.create(user=instace)
        
@receiver(post_save, sender=MyUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()