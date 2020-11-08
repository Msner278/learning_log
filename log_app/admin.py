from django.contrib import admin
from . import models


class TopicAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Topic)
admin.site.register(models.Entry)
