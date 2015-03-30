from datetime import datetime, time
from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.subject.registration.models import RegisteredSubject
from edc.subject.registration.models import BaseRegisteredSubjectModel
from edc.core.identifier.classes import InfantIdentifier


class MaternalPostReg(BaseRegisteredSubjectModel):

    """ Post-partum registration """

    reg_datetime = models.DateTimeField()

    live_infants_to_register = models.IntegerField(
        verbose_name="How many babies are registering to the study? ",
        help_text="",
        )

    maternal_redcap_bid = models.CharField(
        verbose_name="Maternal RedCap Bid",
        max_length=50,
        db_index=True,
#         unique=True,
        null=True,
        blank=True,
        )

    history = AuditTrail()

    def get_registration_datetime(self):
        return self.reg_datetime

    def post_save_register_infants(self, created):
        """Registers infant(s) using the bhp_identifier class which allocates identifiers and creates registered_subject instances.

        Called on the post_save signal"""
        maternal_id = RegisteredSubject.objects.get(subject_identifier=self.registered_subject.subject_identifier)
        if created:
            if self.live_infants_to_register > 0:
                for infant_order in range(0, self.live_infants_to_register):
                    infant_identifier = InfantIdentifier(
                        maternal_identifier=maternal_id.subject_identifier,
                        study_site=maternal_id.study_site,
                        birth_order=infant_order,
                        live_infants=self.live_infants_to_register,
                        live_infants_to_register=self.live_infants_to_register,
                        user=self.user_created)
                    infant_identifier.get_identifier()

    def __unicode__(self):
        return "{0} {1}".format(self.registered_subject, self.reg_datetime)

    def get_report_datetime(self):
        return self.reg_datetime

    def get_absolute_url(self):
        return reverse('admin:eit_maternal_maternalpostreg_change', args=(self.id,))

    class Meta:
        app_label = "eit_maternal"
        verbose_name = "Maternal Post Partum Registration"
