from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Posts(models.Model):
    text = models.TextField()
    image = models.ImageField()
    title = models.CharField(max_length=500)
    user = models.ForeignKey(User, models.CASCADE, default=1)
    date = models.DateField(auto_now=True)

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

