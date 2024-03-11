from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Url(models.Model):
    owner = models.ForeignKey(User, related_name='url', on_delete=models.CASCADE)
    link = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    shortened_link = models.CharField(max_length=100, unique=True)
    clicks = models.IntegerField(default=0)
    expiry_date = models.DateTimeField(blank=True, null=True, default=None)
    customized_link = models.CharField(max_length=100, unique=True, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['owner']),
            models.Index(fields=['shortened_link']),
            models.Index(fields=['customized_link'])
        ]

    def __str__(self) -> str:
        return f"{self.owner}'s url"
