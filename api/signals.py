from .text_summarizer import getSummarization
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Note, Summary


@receiver(post_save, sender=Note)
def create_summary(sender, instance, created, **kwargs):
    summary = getSummarization(instance.body, 5)
    if created:
        Summary.objects.create(associated_note=instance, summary=summary)

# post_save.connect(create_summary, sender=Note)