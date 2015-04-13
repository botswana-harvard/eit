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
        consent = MaternalConsent.objects.get(subject_identifier=cleaned_data.get('registered_subject').relative_identifier)
        if consent.cohort != 'control':
            raise forms.ValidationError('The screening BID is required for the {} cohort. Please fill it in'.format(consent.cohort))

        if MaternalPostReg.objects.filter(registered_subject__subject_identifier=cleaned_data.get('registered_subject').relative_identifier):
            delivery = MaternalPostReg.objects.get(registered_subject__subject_identifier=cleaned_data.get('registered_subject').relative_identifier)
            if not cleaned_data.get('dob', None) == delivery.delivery_datetime.date():
                raise forms.ValidationError('Infant dob must match maternal delivery date of %s. You wrote %s' % (delivery.delivery_datetime.date(), cleaned_data.get('dob', None),))
            if cleaned_data.get('infant_redcap_sbid'):
                birth = InfantBirth.objects.filter(infant_redcap_sbid=cleaned_data.get('infant_redcap_sbid'))
                if birth:
                    raise forms.ValidationError('That Screening bid has already been used for participant {}'.format(birth.registered_subject.subject_identifier))
                match = re.search('S-\d{2}-\d{4}-\d{2}',cleaned_data.get('infant_redcap_sbid'))
                if not match:
                    raise forms.ValidationError('The Screening REDCAP Bid you provided does not conform to the presribed format for Screening')

        return cleaned_data

    class Meta:
        model = InfantBirth


