from django.db import models
from django.conf import settings
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response    
from rest_framework import status

class Session(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    button1_clicks = models.IntegerField(default=0)
    button2_clicks = models.IntegerField(default=0)

    @property
    def session_duration(self):
        if self.end_time:
            return (self.end_time - self.start_time).total_seconds() / 60 
        return None

    def __str__(self):
        return f"Session for {self.user.username}"

class ButtonClick(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    button_number = models.IntegerField()
    click_time = models.DateTimeField(default=timezone.now)