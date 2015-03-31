from django import forms

from edc.subject.registration.models import RegisteredSubject
from edc.base.form.forms import BaseModelForm
from edc.subject.consent.forms import BaseConsentedModelForm

from apps.eit_infant.models import InfantBirth
from apps.eit_maternal.models import MaternalPostReg


class InfantBirthForm (BaseModelForm):
    def clean(self):

        cleaned_data = self.cleaned_data
        if MaternalPostReg.objects.filter(registered_subject__subject_identifier=cleaned_data.get('registered_subject').relative_identifier):
            delivery = MaternalPostReg.objects.get(registered_subject__subject_identifier=cleaned_data.get('registered_subject').relative_identifier)
            if not cleaned_data.get('dob', None) == delivery.delivery_datetime.date():
                raise forms.ValidationError('Infant dob must match maternal delivery date of %s. You wrote %s' % (delivery.delivery_datetime.date(), cleaned_data.get('dob', None),))
        return cleaned_data

    class Meta:
        model = InfantBirth


