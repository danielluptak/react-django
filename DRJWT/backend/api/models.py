from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_customer = models.BooleanField('customer status', default=False)
    is_it = models.BooleanField('IT status', default=False)
    bio = models.CharField(max_length=1000, null=True, blank = True)
    
    def __str__(self):
        return str(self.user)
    
@receiver(post_save, sender=User)
def user_createdr(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance) 
    else:
        instance.profile.save()