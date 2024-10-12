from django.db.models.signals import post_save, pre_delete
from .models import CustomeUser , UserProfile
from django.dispatch import receiver

@receiver(post_save, sender=CustomeUser)
def create_profile(sender, instance, created, **kwargs) : 
    
    if created : # if recently created ...
        UserProfile.objects.create(user=instance)
        
    instance.userprofile.save() # every time user is save User Profile is save
    
    

