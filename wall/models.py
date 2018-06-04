from django.db import models

class Message(models.Model):
    HAPPY = 'HAP'
    SAD = 'SAD'
    ANGRY = 'ANG'
    COOL = 'COO'
    MOOD_CHOICES = (
        (HAPPY, 'Happy mood'),
        (SAD, 'Sad mood'),
        (ANGRY, 'Angry mood'),
        (COOL, 'Cool mood'),
    )
    mood = models.CharField(
        max_length=3,
        choices=MOOD_CHOICES,
        default=HAPPY
    )
    text = models.TextField()
