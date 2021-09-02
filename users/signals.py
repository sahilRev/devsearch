from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# @receiver(post_save, sender=Profile)
def createdProfile(sender, instance, created, **kwargs):
    print('profile signal triggered')
    if created:
        user = instance
        Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name

        )

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print('deleting user ...')

post_save.connect(createdProfile, sender=User)



post_delete.connect(deleteUser, sender=Profile)