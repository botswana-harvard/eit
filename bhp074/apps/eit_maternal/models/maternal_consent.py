from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.subject.registration.models import RegisteredSubject
from edc.subject.consent.models import BaseConsent
from edc.subject.consent.mixins.bw import IdentityFieldsMixin
from edc.subject.consent.mixins import ReviewAndUnderstandingFieldsMixin

from .base_maternal_consent import BaseMaternalConsent


class MaternalConsent(BaseMaternalConsent):

    """Model for maternal consent and registration model for mothers."""

    history = AuditTrail()

    registered_subject = models.OneToOneField(RegisteredSubject,
        editable=False,
        null=True,
        help_text='')

    def get_registered_subject(self):
        return self.registered_subject

    def update_registered_subject_on_post_save(self, using, **kwargs):
        if not self.registered_subject:
            subject = RegisteredSubject.objects.filter(subject_identifier=self.subject_identifier)
            if subject:
                self.registered_subject=subject[0]
                self.save(using=using)
#                 
#     def get_subject_type(self):
#         return 'maternal'
# 
#     def get_subject_identifier(self):
#         return self.subject_identifier
# 
#     @property
#     def is_hiv_positive(self):
#         return 'Yes'
# 
#     def get_result_value(self, attr=None):
#         """Returns a result value for given attr name for the lab_tracker."""
#         retval = None
#         if not attr in dir(self):
#             raise TypeError('Attribute {0} does not exist in model {1}'.format(attr, self._meta.object_name))
#         if attr == 'is_hiv_positive':
#             if self.is_hiv_positive.lower() == 'yes':
#                 retval = 'POS'
#             else:
#                 retval = 'NEG'
#         return retval

    def dispatch_container_lookup(self):
        return None

    @classmethod
    def get_consent_update_model(self):
        return models.get_model('bhp_consent', 'MaternalConsentUpdate')
    
    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalconsent_change', args=(self.id,))

    class Meta:
        verbose_name = "Maternal Consent"
        app_label = 'eit_maternal'


# for field in IdentityFieldsMixin._meta.fields:
#     if field.name not in [fld.name for fld in MaternalConsent._meta.fields]:
#         field.contribute_to_class(MaternalConsent, field.name)
        
# for field in ReviewAndUnderstandingFieldsMixin._meta.fields:
#     if field.name not in [fld.name for fld in MaternalConsent._meta.fields]:
#         field.contribute_to_class(MaternalConsent, field.name)
