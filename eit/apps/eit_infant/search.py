from django.db.models import Q

from edc.dashboard.search.classes import BaseSearchByWord

from .models import InfantBirth


class InfantSearchByWord(BaseSearchByWord):

    name = 'word'
    search_model = InfantBirth
    template = 'infantbirth_include.html'

    @property
    def qset(self):
        qset = (Q(registered_subject__subject_identifier__icontains=self.search_value) |
                Q(registered_subject__first_name__icontains=self.search_value))
        return qset
