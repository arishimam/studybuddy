from django.db import models

from django.conf import settings
# Create your models here.


class AudioFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="audio_files/")


class Note(models.Model):
    audio_file = models.ForeignKey(
        AudioFile, on_delete=models.CASCADE, related_name='notes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

