from django.db import models

class EventFavorite(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="favorite_event")
    user = models.OneToOneField("User", on_delete=models.CASCADE)