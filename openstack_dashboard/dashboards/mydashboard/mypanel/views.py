import json

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms
from horizon import tables
from horizon.utils import memoized
from horizon import workflows

from openstack_dashboard import api
from openstack_dashboard.dashboards.mydashboard.mypanel import constants
from openstack_dashboard.dashboards.mydashboard.mypanel import tables as project_tables

from openstack_dashboard.dashboards.mydashboard.mypanel import forms as project_forms

INDEX_URL = constants.POLICY_INDEX_URL


class IndexView(tables.DataTableView):

    table_class = project_tables.PolicyTable
    template_name = constants.POLICY_TEMPLATE_NAME
    page_title=_("Policy")
    def get_data(self):
        request = self.request
        aggregates = []
        try:
            aggregates = api.nova.policy_list(self.request)
        except Exception:
            exceptions.handle(request,
                              _('Unable to retrieve host aggregates list.'))
        aggregates.sort(key=lambda aggregate: aggregate.name.lower())
        return aggregates

'''
class UpdateView(forms.ModalFormView):
    template_name = constants.POLICY_UPDATE_VIEW_TEMPLATE
    form_class = project_forms.UpdatePolicyForm
    success_url = reverse_lazy(constants.POLICY_INDEX_URL)

    def get_initial(self):
        aggregate = self.get_object()
        return {'id': self.kwargs["id"],
                'name': aggregate.name
                }

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['id'] = self.kwargs['id']
        return context

    def get_object(self):
        if not hasattr(self, "_object"):
            policy_id = self.kwargs['id']
            try:
                self._object = \
                    api.nova.policy_get(self.request, policy_id)
            except Exception:
                msg = _('Unable to retrieve the aggregate to be updated')
                exceptions.handle(self.request, msg)
        return self._object


class CreateView(forms.ModalFormView):
    form_class = project_forms.CreatePolicyForm

    template_name = constants.POLICY_CREATE_VIEW_TEMPLATE
    context_object_name = 'policy'
    success_url = reverse_lazy("horizon:mydashboard:policy:index")
'''
