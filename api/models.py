from django.db import models
import uuid
# Create your models here.
class Event(models.Model):
    session_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Data(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='data',
    )
    host = models.CharField(max_length=250)
    path = models.CharField(max_length=100)
    element = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.host} - {self.path}"

class Form(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    data = models.ForeignKey(
        Data,
        on_delete=models.CASCADE,
        related_name='form',
    )

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"