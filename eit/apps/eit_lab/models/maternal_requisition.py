from django.core.urlresolvers import reverse
from django.db import models

from edc.audit.audit_trail import AuditTrail
from edc.lab.lab_requisition.models import BaseClinicRequisition
# from edc.entry_meta_data.managers import RequisitionMetaDataManager

from eit.apps.eit_maternal.models import MaternalVisit
from eit.apps.eit_lab.managers import RequisitionManager

from .aliquot_type import AliquotType
from .packing_list import PackingList
from .panel import Panel


class MaternalRequisition(BaseClinicRequisition):

    maternal_visit = models.ForeignKey(MaternalVisit)

    entry_meta_data_manager = RequisitionManager(MaternalVisit)

    packing_list = models.ForeignKey(PackingList, null=True, blank=True)

    aliquot_type = models.ForeignKey(AliquotType)

    panel = models.ForeignKey(Panel)

    history = AuditTrail()

    def get_visit(self):
        return self.maternal_visit

    def aliquot(self):
        url = reverse('admin:eit_lab_aliquot_changelist')
        return """<a href="{url}?q={requisition_identifier}" />aliquot</a>""".format(url=url, requisition_identifier=self.requisition_identifier)
    aliquot.allow_tags = True

    class Meta:
        app_label = 'eit_lab'
        verbose_name = 'Maternal Laboratory Requisition'
        unique_together = ('maternal_visit', 'panel', 'is_drawn')
