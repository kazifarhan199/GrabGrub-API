from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save

User = get_user_model()


class Posts(models.Model):
    text = models.TextField()
    image = models.ImageField()
    title = models.CharField(max_length=500)
    user = models.ForeignKey(User, models.CASCADE)
    date = models.DateField(auto_now=True)
    servings = models.IntegerField()

    @property
    def likes(self):
        count = trackLikes.objects.filter(post=self).count()
        return count
    
    @property
    def comments(self):
        return len([1, 2])

    def __str__(self):
        return self.title    

class trackLikes(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    post = models.ForeignKey(Posts, models.CASCADE)
    class Meta:
       unique_together = ("user", "post")


class Claim(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    post = models.ForeignKey(Posts, models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.user.username +'-'+str(self.post)+'-'+str(self.quantity)

def create_claim(sender, instance, **kwargs):
    if instance.quantity > instance.post.servings:
        raise ValueError("Not enough quantity")
    else:
        post = instance.post
        post.servings = post.servings - instance.quantity
        post.save()

post_save.connect(create_claim, sender=Claim)
