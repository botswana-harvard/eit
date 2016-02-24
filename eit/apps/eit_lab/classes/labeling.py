from edc.subject.registration.models import RegisteredSubject

from lis.labeling.classes import ModelLabel
from lis.labeling.models import ZplTemplate


class EitAliquotLabeling(ModelLabel):

    def __init__(self):
        super(EitAliquotLabeling, self).__init__()
        self.zpl_template = ZplTemplate.objects.get(name='aliquot_label')

    def refresh_label_context(self):
        aliquot = self.model_instance
        subject_identifier = aliquot.get_subject_identifier()
        registered_subject = RegisteredSubject.objects.get(subject_identifier=subject_identifier)
        primary = ''
        if aliquot.aliquot_identifier[-2:] == '01':
            primary = "<"
        custom = {}
        custom.update({
            'aliquot_identifier': aliquot.aliquot_identifier,
            'aliquot_count': aliquot.aliquot_identifier[-2:],
            'primary': primary,
            'barcode_value': aliquot.barcode_value(),
            'protocol': aliquot.aliquot_identifier[0:3],
            'site': aliquot.aliquot_identifier[3:5],
            'clinician_initials': aliquot.receive.clinician_initials,
            'drawn_datetime': aliquot.receive.drawn_datetime,
            'subject_identifier': subject_identifier,
            'gender': registered_subject.gender,
            'dob': registered_subject.dob,
            'initials': registered_subject.initials,
            'panel': aliquot.panel(),
            'aliquot_type': aliquot.aliquot_type.alpha_code.upper()})
        self.label_context.update(**custom)
