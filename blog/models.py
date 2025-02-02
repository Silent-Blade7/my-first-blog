from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):  # models.model so django knows to saves it in the database
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # this is a link to another model
    title = models.CharField(max_length=200)  # define text with limited characters
    text = models.TextField()  # for long text with no limit
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
