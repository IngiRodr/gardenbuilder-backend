from django.db import models
from django.utils.timezone import now
from gardens.models import Garden


class Bed(models.Model):
    name = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    garden = models.ForeignKey(
        Garden, related_name="beds", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    start_date = models.DateField(default=now)
    length = models.PositiveSmallIntegerField(default=0)
    width = models.PositiveSmallIntegerField(default=0)
    notes = models.CharField(max_length=500)

    def __str__(self):
        return self.bed_name

    class Meta:
        ordering = ["created"]
