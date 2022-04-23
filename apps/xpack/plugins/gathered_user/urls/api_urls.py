# -*- coding: utf-8 -*-
#
from django.urls import path
from rest_framework.routers import DefaultRouter

from .. import api

router = DefaultRouter()
router.register('tasks', api.GatherUserTaskViewSet, 'task')
router.register('task-executions', api.GatherUserTaskExecutionViewSet, 'task-execution')

urlpatterns = [
]
urlpatterns += router.urls
