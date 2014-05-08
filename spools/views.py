from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView

from .models import SidebarItem, Thumper
from .forms import ThumperForm

class DetailView(generic.DetailView):
    model = Thumper
    template_name = 'spools/thumper_detail.html'


class IndexView(generic.ListView):
    template_name = 'spools/thumper_index.html'
    context_object_name = 'latest_thumper_list'

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            thumper_form = ThumperForm(request.POST)
            if thumper_form.is_valid():
                new_thumper = thumper_form.save()

            return HttpResponseRedirect(request.path)

        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = ThumperForm()
        context['sidebar_items_list'] = SidebarItem.objects.order_by('-position')
        return context

    def get_queryset(self):
        """
        Return the last 10 thumpers.
        """
        return Thumper.objects.order_by('-created_at')[:10]
