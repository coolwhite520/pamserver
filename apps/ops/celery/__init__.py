# -*- coding: utf-8 -*-

import os

from kombu import Exchange, Queue
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pamserver.settings')
from pamserver import settings
# from django.conf import settings

app = Celery('pamserver')

configs = {k: v for k, v in settings.__dict__.items() if k.startswith('CELERY')}
# Using a string here means the worker will not have to
# pickle the object when using Windows.
# app.config_from_object('django.conf:settings', namespace='CELERY')
configs["CELERY_QUEUES"] = [
    Queue("celery", Exchange("celery"), routing_key="celery"),
    Queue("ansible", Exchange("ansible"), routing_key="ansible"),
]

app.namespace = 'CELERY'
app.conf.update(configs)
app.autodiscover_tasks(lambda: [app_config.split('.')[0] for app_config in settings.INSTALLED_APPS])
