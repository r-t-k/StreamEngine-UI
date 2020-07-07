from functools import partial
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string
import uuid

make_stream_key = partial(get_random_string, 20)



class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    channels = models.TextField(blank=True)
    privs = models.TextField(blank=True)
    subs = models.TextField(blank=True)

    def __str__(self):
        return self.username


class Channel(models.Model):
    cid = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    vods = models.TextField(blank=True)
    moderators = models.ManyToManyField(CustomUser, related_name="moderators")
    streamkey = models.UUIDField(default=uuid.uuid4, unique=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_live= models.BooleanField(default=False)
