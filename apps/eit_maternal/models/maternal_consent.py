from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.subject.registration.models import RegisteredSubject

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

    def dispatch_container_lookup(self):
        return None

    @classmethod
    def get_consent_update_model(self):
        return models.get_model('bhp_consent', 'MaternalConsentUpdate')

    class Meta:
        verbose_name = "Maternal Consent"
        app_label = 'eit_maternal'

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalconsent_change', args=(self.id,))
