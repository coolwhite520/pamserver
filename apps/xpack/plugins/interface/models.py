# -*- coding: utf-8 -*-
#

import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from pamserver.context_processor import default_interface


class Interface(models.Model):
    PATH_LOGO = 'xpack/logo/'

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    login_title = models.CharField(
        max_length=1024, null=True, blank=True,
        verbose_name=_('Title of login page')
    )
    login_image = models.ImageField(
        upload_to=PATH_LOGO, max_length=128, null=True, blank=True,
        verbose_name=_('Image of login page')
    )
    favicon = models.ImageField(
        upload_to=PATH_LOGO, max_length=128, null=True, blank=True,
        verbose_name=_('Website icon')
    )
    logo_index = models.ImageField(
        upload_to=PATH_LOGO, max_length=128,  null=True, blank=True,
        verbose_name=_('Logo of management page')
    )
    logo_logout = models.ImageField(
        upload_to=PATH_LOGO, max_length=128, null=True, blank=True,
        verbose_name=_('Logo of logout page')
    )

    class Meta:
        verbose_name = _('Interface setting')

    @classmethod
    def get_interface_setting(cls):
        from django.db.models.fields.files import ImageFieldFile
        data = {k: v for k, v in default_interface.items()}
        interface = cls.objects.first()

        if not interface:
            return data

        for k in data:
            attr = getattr(interface, k, '')
            if attr:
                data[k] = attr.url if isinstance(attr, ImageFieldFile) else attr
        return data

    @classmethod
    def interface(cls):
        interface = cls.objects.first()
        return interface
