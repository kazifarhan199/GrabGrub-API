from django.contrib import admin
from .models import Posts, trackLikes, Claim

admin.site.register(Posts)
admin.site.register(trackLikes)
admin.site.register(Claim)
