from __future__ import absolute_import

from django.urls import path

from .. import api

urlpatterns = [
    path('setting', api.InterfaceApi.as_view(), name='interface-setting'),
    path('restore', api.RestoreDefaultView.as_view(), name='interface-restore')
]
