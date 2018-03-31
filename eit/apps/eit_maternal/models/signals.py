from django.db.models.signals import post_save
from django.dispatch import receiver

from .maternal_post_reg import MaternalPostReg
from .maternal_consent import MaternalConsent


@receiver(post_save, weak=False, dispatch_uid='post_save_register_infants')
def post_save_register_infants(sender, instance, raw, created, using, **kwarg):
    if isinstance(instance, MaternalPostReg):
        i_indicator = instance.live_infants_to_register
        while i_indicator > 0:
            instance.post_save_register_infants(created, i_indicator)
            i_indicator = i_indicator - 1


@receiver(post_save, weak=False, dispatch_uid='update_registered_subject_on_post_save')
def update_registered_subject_on_post_save(sender, instance, raw, created, using, **kwarg):
    if isinstance(instance, MaternalConsent):
        instance.update_registered_subject_on_post_save(using)
