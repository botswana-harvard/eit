from django.contrib import admin

from edc.subject.consent.admin import BaseConsentModelAdmin, BaseConsentUpdateModelAdmin, BaseConsentUpdateInlineAdmin

from ..models import MaternalConsent
from ..forms import MaternalConsentForm


class MaternalConsentAdmin(BaseConsentModelAdmin):

    form = MaternalConsentForm

    def __init__(self, *args, **kwargs):
        super(MaternalConsentAdmin, self).__init__(*args, **kwargs)
        # remove these fields from admin fields list, default values should apply
        for fld in ['witness_name', 'is_literate', 'guardian_name', 'is_incarcerated',
                    'language', 'confirm_identity', 'may_store_samples', 'consent_reviewed',
                    'study_questions', 'assessment_score', 'consent_copy', 'identity_type',
                    'comment', 'is_dob_estimated', 'gender']:
            self.fields.remove(fld)
        for fld in ["cohort", ]:
            self.fields.append(fld)

    radio_fields = {
        "cohort": admin.VERTICAL,
    }

    def save_model(self, request, obj, form, change):
        """Saves and randomizes."""
        if not change:
            obj.may_store_samples = 'Yes'
            obj.is_incarcerated = 'No'
            obj.is_literate = 'No'
            obj.language = 'tn'
            obj.is_verified = True
            obj.confirm_identity = obj.identity
            obj.identity_type = 'OMANG'
            obj.gender = 'F'
        return super(MaternalConsentAdmin, self).save_model(request, obj, form, change)

admin.site.register(MaternalConsent, MaternalConsentAdmin)
