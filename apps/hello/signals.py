#!/usr/bin/env python
# -*- coding: utf-8 -*-
from apps.hello.models import EntryChange
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

__author__ = 'Odarchenko N.D.'


@receiver(post_save)
def model_save_handler(sender, created, **kwargs):
    class_name = sender.__name__
    if class_name == "EntryChange":
        # avoid recursive call
        return
    action = "create" if created else "update"
    EntryChange.objects.create(model=class_name, action=action).save()


@receiver(post_delete)
def model_delete_handler(sender, **kwargs):
    class_name = sender.__name__
    EntryChange.objects.create(model=class_name, action="delete").save()
