from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models, IntegrityError

from edc.audit.audit_trail import AuditTrail
from edc.entry_meta_data.models import ScheduledEntryMetaData, RequisitionMetaData
from edc.subject.visit_tracking.models import BaseVisitTracking
from edc.subject.visit_tracking.settings import VISIT_REASON_NO_FOLLOW_UP_CHOICES

from ..choices import VISIT_REASON, ALIVE_DEAD_UNKNOWN


class MaternalVisit(BaseVisitTracking):

    """ Maternal visit form that links all follow-up forms """

    history = AuditTrail()

    survival_status = models.CharField(
        max_length=10,
        verbose_name="Survival status",
        choices=ALIVE_DEAD_UNKNOWN,
        null=True,
        blank=False)

    date_last_alive = models.DateField(
        verbose_name="Date last known alive",
        help_text="",
        null=True,
        blank=True
        )

    @property
    def registered_subject(self):
        return self.get_registered_subject()

    def __unicode__(self):
        return unicode(self.appointment)

    def get_visit_reason_choices(self):
        return VISIT_REASON

    def get_visit_reason_no_follow_up_choices(self):
        """Returns the visit reasons that do not imply any data collection; that is, the subject is not available."""
        dct = {}
        if self.appointment.visit_definition.code == '2180M':
            return dct
        else:
            for item in VISIT_REASON_NO_FOLLOW_UP_CHOICES:
                dct.update({item: item})
            dct.update({'vital status': 'vital status'})
            del dct['death']
            del dct['lost']
            return dct

    def save(self, *args, **kwargs):
        super(MaternalVisit, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalvisit_change', args=(self.id,))

    class Meta:
        verbose_name = "Maternal Visit"
        app_label = "eit_maternal"
