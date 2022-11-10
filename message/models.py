from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Message(models.Model):
    user =  models.ForeignKey(User, models.CASCADE)
    to = models.ForeignKey(User, models.CASCADE, related_name='to')
    text = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username + ' -> ' + self.to.username
