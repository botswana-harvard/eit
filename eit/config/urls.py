from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic import RedirectView
from django.db.models import get_models
import django_databrowse

from edc.subject.rule_groups.classes import site_rule_groups
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.dashboard.section.classes import site_sections
from edc.subject.visit_schedule.classes import site_visit_schedules
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.dashboard.subject.views import additional_requisition

from django.contrib import admin

admin.autodiscover()
site_lab_profiles.autodiscover()
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

from eit.apps.eit.eit_app_configuration.classes import EitAppConfiguration

EitAppConfiguration().prepare()
site_visit_schedules.autodiscover()
site_visit_schedules.build_all()
site_rule_groups.autodiscover()
site_lab_tracker.autodiscover()
# data_manager.prepare()
site_sections.autodiscover()
site_sections.update_section_lists()

APP_NAME = settings.APP_NAME

for model in get_models():
    try:
        django_databrowse.site.register(model)
    except:
        pass

urlpatterns = patterns(
    '',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/logout/$', RedirectView.as_view(url='/{app_name}/logout/'.format(app_name=APP_NAME))),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
    '',
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)
# this is for additional_requisitions
urlpatterns += patterns(
    '',
    url(r'^{app_name}/dashboard/visit/add_requisition/'.format(app_name=APP_NAME),
        additional_requisition,
        name="add_requisition"),
)

urlpatterns += patterns(
    '',
    url(r'^databrowse/(.*)', login_required(django_databrowse.site.root)),
)

urlpatterns += patterns(
    '',
    url(r'^{app_name}/section/labclinic/'.format(app_name=APP_NAME),
        include('edc.lab.lab_clinic_api.urls'), name="section_url_name"),
)

urlpatterns += patterns(
    '',
    url(r'^{app_name}/dashboard/'.format(app_name=APP_NAME),
        include('eit.apps.{app_name}_dashboard.urls'.format(app_name=APP_NAME))),
)

urlpatterns += patterns(
    '',
    url(r'^{app_name}/login/'.format(app_name=APP_NAME),
        'django.contrib.auth.views.login',
        name='{app_name}_login'.format(app_name=APP_NAME)),
    url(r'^{app_name}/logout/'.format(app_name=APP_NAME),
        'django.contrib.auth.views.logout_then_login',
        name='{app_name}_logout'.format(app_name=APP_NAME)),
    url(r'^{app_name}/password_change/'.format(app_name=APP_NAME),
        'django.contrib.auth.views.password_change',
        name='password_change_url'.format(app_name=APP_NAME)),
    url(r'^{app_name}/password_change_done/'.format(app_name=APP_NAME),
        'django.contrib.auth.views.password_change_done',
        name='password_change_done'.format(app_name=APP_NAME)),
)

urlpatterns += patterns(
    '',
    url(r'^{app_name}/section/'.format(app_name=APP_NAME), include('edc.dashboard.section.urls'), name='section'),
)

urlpatterns += patterns(
    '',
    url(r'^{app_name}/$'.format(app_name=APP_NAME),
        RedirectView.as_view(url='/{app_name}/section/'.format(app_name=APP_NAME))),
    url(r'', RedirectView.as_view(url='/{app_name}/section/'.format(app_name=APP_NAME))),
)

urlpatterns += staticfiles_urlpatterns()
