from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from spools.models import SidebarItem, Spool, Thumper

class IndexView(generic.ListView):
    template_name = 'spools/spool_index.html'
    context_object_name = 'latest_spool_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['sidebar_items_list'] = SidebarItem.objects.order_by('-position')
        return context

    def get_queryset(self):
        """
        Return the last 10 spools.
        """
        return Spool.objects.order_by('-created_at')[:10]


class DetailView(generic.DetailView):
    model = Spool
    template_name = 'spools/spool_detail.html'
