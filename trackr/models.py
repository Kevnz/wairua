from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MoodEntry(models.Model):
    MOODS = (
        ('😄', '😄 Happy'),
        ('🙁', '🙁 Unhappy'),
        ('😀', '😀 Really Good'),
        ('😠', '😠 Angry'),
        ('🤬', '🤬 Really Angry'),
        ('😢', '😢 Sad'),
        ('😩', '😩 Weary'),
        ('🤢', '🤢 Sick'),
        ('💩', '💩 Poop'),
        ('🤣', '🤣 ROFL'),
        ('😑', '😑 Detached'),
        ('🤔', '🤔 Contemplative'),
        ('😳', '😳 Shocked'),
    )
    selected_mood = models.CharField(max_length=1, choices=MOODS, blank=True, default='😄', help_text="Select your current Mood")

    details = models.CharField(max_length=500, help_text="Enter details about your mood")

    enteredOn = models.DateTimeField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Metadata
    class Meta:
        ordering = ["-enteredOn"]

