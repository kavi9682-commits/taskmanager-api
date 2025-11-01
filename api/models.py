from django.db import models
from django.conf import settings
# Create your models here.

class Task(models.Model):
    owner= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='tasks',
        on_delete= models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.title} ({'done' if self.completed else 'pending'})"