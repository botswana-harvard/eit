from django.conf import settings

from edc.core.identifier.classes import BaseIdentifier


class OrderIdentifier(BaseIdentifier):

    def __init__(self):
        identifier_format = '074{site}{sequence}'
        app_name = 'eit_lab'
        model_name = 'orderidentifierhistory'
        modulus = 11
        self.community = settings.SITE_CODE
        super(OrderIdentifier, self).__init__(identifier_format=identifier_format,
                                              app_name=app_name, model_name=model_name, modulus=modulus)
