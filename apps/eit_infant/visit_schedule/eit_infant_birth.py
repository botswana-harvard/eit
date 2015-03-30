from collections import OrderedDict

from edc.subject.visit_schedule.classes import VisitScheduleConfiguration, site_visit_schedules, EntryTuple, MembershipFormTuple, ScheduleGroupTuple, RequisitionPanelTuple
from edc.constants import REQUIRED, NOT_REQUIRED, ADDITIONAL, NOT_ADDITIONAL

from apps.eit_infant.models import InfantVisit, InfantBirth

#from ...eit_maternal.models import MaternalConsent


class EitInfantBirthVisitSchedule(VisitScheduleConfiguration):

    name = 'birth visit schedule'
    app_label = 'eit_infant'
    # membership forms
    # (name, model, visible)
    membership_forms = OrderedDict({
        'infant_birth_record': MembershipFormTuple('infant_birth_record', InfantBirth, True),
        })

    # schedule groups
    # (name, membership_form_name, grouping_key, comment)
    schedule_groups = OrderedDict({
        'Infant Birth': ScheduleGroupTuple('Infant Birth', 'infant_birth_record', None, None),
        })

    # visit_schedule
    # see edc.subject.visit_schedule.models.visit_defintion
    visit_definitions = OrderedDict()
    visit_definitions['1000'] = {
            'title': 'Screening 1',
            'time_point': 0,
            'base_interval': 0,
            'base_interval_unit': 'D',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                #(entry_order, app_label, model_name, requisition_panel_name, panel_type, aliquot_type_alpha_code, form_visible)
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (

            )}
    visit_definitions['1010'] = {
            'title': 'Screening 2',
            'time_point': 1,
            'base_interval': 1,
            'base_interval_unit': 'D',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                #(entry_order, app_label, model_name, requisition_panel_name, panel_type, aliquot_type_alpha_code, form_visible)
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (

            )}
    visit_definitions['2001'] = {
            'title': 'Enrollment Visit',
            'time_point': 10,
            'base_interval': 10,
            'base_interval_unit': 'D',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                #(entry_order, app_label, model_name, requisition_panel_name, panel_type, aliquot_type_alpha_code, form_visible)
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (

            )}
    visit_definitions['2002'] = {
            'title': 'Infant 2 Weeks Visit',
            'time_point': 20,
            'base_interval': 20,
            'base_interval_unit': 'D',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                #(entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}

    visit_definitions['2003'] = {
            'title': 'Infant 3 Weeks Visit',
            'time_point': 30,
            'base_interval': 30,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2004'] = {
            'title': 'Infant 4 Weeks Visit',
            'time_point': 40,
            'base_interval': 4,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2005'] = {
            'title': 'Infant 5 Weeks Visit',
            'time_point': 50,
            'base_interval': 5,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2006'] = {
            'title': 'Infant 6 Weeks Visit',
            'time_point': 60,
            'base_interval': 6,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2007'] = {
            'title': 'Infant 7 Weeks Visit',
            'time_point': 70,
            'base_interval': 70,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2008'] = {
            'title': 'Infant 8 Weeks Visit',
            'time_point': 80,
            'base_interval': 8,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2012'] = {
            'title': 'Infant 12 Weeks Visit',
            'time_point': 120,
            'base_interval': 120,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2024'] = {
            'title': 'Infant 24 Weeks Visit',
            'time_point': 240,
            'base_interval': 240,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2036'] = {
            'title': 'Infant 36 Weeks Visit',
            'time_point': 360,
            'base_interval': 360,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2048'] = {
            'title': 'Infant 48 Weeks Visit',
            'time_point': 480,
            'base_interval': 48,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2060'] = {
            'title': 'Infant 60 Weeks Visit',
            'time_point': 600,
            'base_interval': 60,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2072'] = {
            'title': 'Infant 72 Weeks Visit',
            'time_point': 720,
            'base_interval': 720,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2084'] = {
            'title': 'Infant 84 Weeks Visit',
            'time_point': 840,
            'base_interval': 840,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2096'] = {
            'title': 'Infant 96 Weeks Visit',
            'time_point': 960,
            'base_interval': 960,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2120'] = {
            'title': 'Infant 120 Weeks Visit',
            'time_point': 1200,
            'base_interval': 1200,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2132'] = {
            'title': 'Infant 132 Weeks Visit',
            'time_point': 1320,
            'base_interval': 1320,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2144'] = {
            'title': 'Infant 144 Weeks Visit',
            'time_point': 1440,
            'base_interval': 1440,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2156'] = {
            'title': 'Infant 156 Weeks Visit',
            'time_point': 1560,
            'base_interval': 1560,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2168'] = {
            'title': 'Infant 168 Weeks Visit',
            'time_point': 1680,
            'base_interval': 1680,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2180'] = {
            'title': 'Infant 180 Weeks Visit',
            'time_point': 1800,
            'base_interval': 1800,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}
    visit_definitions['2192'] = {
            'title': 'Infant 192 Weeks Visit',
            'time_point': 1920,
            'base_interval': 1920,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'eit_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'eit_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'eit_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'eit_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'eit_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'eit_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'eit_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'eit_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'eit_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
            )}

site_visit_schedules.register(EitInfantBirthVisitSchedule)
