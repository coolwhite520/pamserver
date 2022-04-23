# -*- coding: utf-8 -*-
#

from django.urls import path

from .. import views


urlpatterns = [
    path('license/', views.LicenseDetailView.as_view(), name='license-detail'),
    path('license/import/', views.ImportLicenseView.as_view(), name='license-import'),
]
