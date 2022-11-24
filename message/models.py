from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Posts

User = get_user_model()


class Message(models.Model):
    user =  models.ForeignKey(User, models.CASCADE)
    to = models.ForeignKey(User, models.CASCADE, related_name='to')
    post = models.ForeignKey(Posts, models.CASCADE, blank=True, null=True)
    text = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='message')
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ' -> ' + self.to.username

class Conversation(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    to = models.ForeignKey(User, models.CASCADE, related_name='cto')

    class Meta:
        unique_together = ('user', 'to')

    def __str__(self):
        return self.user.username + ' -> ' + self.to.username

from django.db.models.signals import post_save

def createConversation(sender, instance, **kwargs):
    if (instance.user != instance.to):
        [i.delete() for i in Conversation.objects.filter(user=instance.user, to=instance.to)]
        Conversation.objects.create(user=instance.user, to=instance.to)
    [i.delete() for i in Conversation.objects.filter(user=instance.to, to=instance.user)]
    Conversation.objects.create(user=instance.to, to=instance.user)


post_save.connect(createConversation, sender=Message)
