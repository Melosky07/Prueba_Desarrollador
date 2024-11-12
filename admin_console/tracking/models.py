from django.db import models
from django.conf import settings
from django.utils import timezone

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
    button_number = models.IntegerField()  # Número del botón (1 o 2)
    click_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Button {self.button_number} click at {self.click_time} for session {self.session.id}"
