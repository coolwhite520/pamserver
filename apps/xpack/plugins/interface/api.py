# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from rest_framework import generics
from rest_framework.response import Response

from xpack.permissions import RBACLicensePermission
from .serializers import InterfaceSerializer
from .models import Interface


class InterfaceApi(generics.RetrieveUpdateAPIView):
    queryset = Interface.objects.all()
    permission_classes = (RBACLicensePermission,)
    serializer_class = InterfaceSerializer
    rbac_perms = {
        'GET': 'settings.change_interface',
        'PUT': 'settings.change_interface',
    }

    def get_object(self):
        obj = Interface.get_interface_setting()
        return obj

    def get(self, request, *args, **kwargs):
        result = self.get_object()
        return Response(result)

    def put(self, request, *args, **kwargs):
        obj = Interface.interface()
        interface_serializer = InterfaceSerializer(instance=obj, data=request.data)
        if interface_serializer.is_valid():
            interface_serializer.save()
            result = self.get_object()
            return Response(result)
        else:
            return Response(interface_serializer.errors, status=400)


class RestoreDefaultView(generics.RetrieveAPIView):
    permission_classes = (RBACLicensePermission,)
    rbac_perms = {
        'GET': 'xpack.change_interface'
    }

    def get(self, request, *args, **kwargs):
        interface = Interface.objects.all()

        if not interface:
            error = {"error": _("It is already in the default setting state!")}
            return Response(error, status=400)
        interface.delete()
        return Response({"success": _("Restore default successfully.")})
