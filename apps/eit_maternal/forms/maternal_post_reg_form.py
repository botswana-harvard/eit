from django import forms

from edc.subject.consent.forms import BaseConsentedModelForm

from ..models import MaternalPostReg


class MaternalPostRegForm (BaseConsentedModelForm):
    def clean(self):

        cleaned_data = self.cleaned_data
        return self.cleaned_data

    class Meta:
        model = MaternalPostReg
