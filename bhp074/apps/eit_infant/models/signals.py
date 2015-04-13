from django.db.models.signals import post_save
from django.dispatch import receiver

from .infant_birth import InfantBirth
from .infant_visit import InfantVisit


# @receiver(post_save, weak=False, dispatch_uid="infant_eligibility_on_post_save")
# def infant_eligibility_on_post_save(sender, instance, raw, created, using, **kwargs):
#     """"""
#     if isinstance(instance, (InfantEligibility)):
#         instance.prepare_appointments(using)

        
@receiver(post_save, weak=False, dispatch_uid='delete_control_apps_post_save')
def delete_control_apps_post_save(sender, instance, **kwargs):
    if isinstance(instance, (InfantBirth)):
        instance.delete_control_apps_post_save()
