from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from rest_framework.authtoken.models import Token

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    image = models.ImageField(upload_to='profile')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

@property
def token(self):
    return str(Token.objects.get_or_create(user=self)[0])

@property
def image(self):
    return str(self.profile.image.url)

@property
def bio(self):
    return str(self.profile.bio)

# User._meta.get_field('email')._unique = True
User.add_to_class('token', token)
User.add_to_class('image', image)
User.add_to_class('bio', bio)


def create_profile(sender, instance, **kwargs):
    if not Profile.objects.filter(user=instance).exists():
        Profile.objects.create(user=instance, image='image/default_profile.jpg')

post_save.connect(create_profile, sender=User)
