from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User


# class to create model for topics
class Topic(models.Model):
    text = models.CharField(_("Text"), max_length=200)
    create_at = models.DateTimeField(_("Create Time"), default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


# class to create model for some log related to a topic
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(_("Text"))
    create_at = models.DateTimeField(_("Create Time"), auto_now_add=True)

    class Meta:
        verbose_name_plural = _('entries')

    def __str__(self):
        return self.topic.text
