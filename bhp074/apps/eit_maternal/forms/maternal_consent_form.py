from django import forms
import re

from edc.subject.consent.forms import BaseSubjectConsentForm, BaseConsentUpdateForm

from ..models import MaternalConsent


class MaternalConsentForm (BaseSubjectConsentForm):

    def clean(self):

        cleaned_data = self.cleaned_data
        consent = MaternalConsent.objects.filter(identity=cleaned_data.get('identity'))
        if consent:
            raise forms.ValidationError("This identity number already exists")
#         if not cleaned_data.get('cohort') and not cleaned_data.get('redcap_bid'):
#             raise forms.ValidationError("This is a required field. Please fill it in.")
#         if cleaned_data.get('cohort')=='control':
#             match = re.search('C-3\d{2}-2-\d',cleaned_data.get('redcap_bid'))
#             if not match:
#                 raise forms.ValidationError('The REDCAP Bid you provided does not conform to the presribed format for Control')
#         elif cleaned_data.get('cohort')=='antepartum':
#             match = re.search('M-1\d{2}-2-\d',cleaned_data.get('redcap_bid'))
#             if not match:
#                 raise forms.ValidationError('The REDCAP Bid you provided does not conform to the presribed format for Antepartum')
#         elif cleaned_data.get('cohort')=='peripartum':
#             match = re.search('M-2\d{2}-2-\d',cleaned_data.get('redcap_bid'))
#             if not match:
#                 raise forms.ValidationError('The REDCAP Bid you provided does not conform to the presribed format for Peripartum')

        return cleaned_data

    class Meta:
        model = MaternalConsent
