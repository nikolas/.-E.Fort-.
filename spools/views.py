from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from spools.models import Spool, Thumper

class IndexView(generic.ListView):
    template_name = 'spools/spool_index.html'
    context_object_name = 'latest_spool_list'

    def get_queryset(self):
        """
        Return the last 10 spools.
        """
        return Spool.objects.order_by('-created_at')[:10]


class DetailView(generic.DetailView):
    model = Spool
    template_name = 'spools/spool_detail.html'
