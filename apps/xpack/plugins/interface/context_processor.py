from .models import Interface


def interface_processor(request):
    context = {}
    interface = Interface.interface()
    if interface:
        if interface.logo_logout:
            context.update({'LOGO_URL': interface.logo_logout.url})
        if interface.logo_index:
            context.update({'LOGO_TEXT_URL': interface.logo_index.url})
        if interface.login_image:
            context.update({'LOGIN_IMAGE_URL': interface.login_image.url})
        if interface.favicon:
            context.update({'FAVICON_URL': interface.favicon.url})
        if interface.login_title:
            context.update({'JMS_TITLE': interface.login_title})
    return context

