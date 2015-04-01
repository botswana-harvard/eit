from django import forms
import re

from edc.subject.registration.models import RegisteredSubject
from edc.base.form.forms import BaseModelForm
from edc.subject.consent.forms import BaseConsentedModelForm

from apps.eit_infant.models import InfantBirth
from apps.eit_maternal.models import MaternalPostReg, MaternalConsent


class InfantBirthForm (BaseModelForm):
    def clean(self):

        cleaned_data = self.cleaned_data
        if MaternalPostReg.objects.filter(registered_subject__subject_identifier=cleaned_data.get('registered_subject').relative_identifier):
            delivery = MaternalPostReg.objects.get(registered_subject__subject_identifier=cleaned_data.get('registered_subject').relative_identifier)
            if not cleaned_data.get('dob', None) == delivery.delivery_datetime.date():
                raise forms.ValidationError('Infant dob must match maternal delivery date of %s. You wrote %s' % (delivery.delivery_datetime.date(), cleaned_data.get('dob', None),))
#         consent = MaternalConsent.objects.get(registered_subject__subject_identifier=cleaned_data.get('registered_subject').relative_identifier)
#         if consent.cohort=='control':
#             match = re.search('C-3\d{2}-1-\d',cleaned_data.get('redcap_bid'))
#             if not match:
#                 raise forms.ValidationError('The REDCAP Bid you provided does not conform to the prescribed format for Control')
#         elif consent.cohort=='antepartum':
#             match = re.search('A-1\d{2}-1-\d',cleaned_data.get('redcap_bid'))
#             if not match:
#                 raise forms.ValidationError('The REDCAP Bid you provided does not conform to the prescribed format for Antepartum')
#         elif consent.cohort=='peripartum':
#             match = re.search('P-2\d{2}-1-\d',cleaned_data.get('redcap_bid'))
#             if not match:
#                 raise forms.ValidationError('The REDCAP Bid you provided does not conform to the prescribed format for Peripartum')

        return cleaned_data

    class Meta:
        model = InfantBirth


