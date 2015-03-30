from django.contrib import admin

from edc.base.modeladmin.admin import BaseModelAdmin, BaseTabularInline
from edc.subject.registration.admin import BaseRegisteredSubjectModelAdmin

from ..forms import MaternalPostRegForm #, MaternalPostFuDxTForm)
from ..models import MaternalPostReg


class MaternalPostRegAdmin(BaseRegisteredSubjectModelAdmin):
    form = MaternalPostRegForm
admin.site.register(MaternalPostReg, MaternalPostRegAdmin)