from django.db import models
from django.conf import settings


class Task(models.Model):
    name = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name="tasks",
                            on_delete=models.CASCADE,
                            null=True,
                            )
