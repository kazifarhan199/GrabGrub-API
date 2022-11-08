from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Posts(models.Model):
    text = models.TextField()
    image = models.ImageField()
    user = models.ForeignKey(User, models.CASCADE, default=1)

    @property
    def likes(self):
        return len([1, 2])
    
    @property
    def comments(self):
        return len([1, 2])

    def __str__(self):
        return self.text    
