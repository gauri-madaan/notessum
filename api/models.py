from django.db import models


class Note(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:20]

class Summary(models.Model):
    associated_note = models.OneToOneField(Note, on_delete=models.CASCADE, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.associated_note.body[:20]
