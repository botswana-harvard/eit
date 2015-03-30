from django import forms

from edc.subject.registration.models import RegisteredSubject
from edc.base.form.forms import BaseModelForm

from bhp074.apps.eit_infant.models import InfantBirth
from edc.subject.consent.forms import BaseConsentedModelForm


class InfantBirthForm (BaseModelForm):
    def clean(self):

        cleaned_data = self.cleaned_data
        return cleaned_data

    class Meta:
        model = InfantBirth


