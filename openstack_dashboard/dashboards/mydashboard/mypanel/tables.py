from django.template import defaultfilters as filters
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy

import logging
import six

from horizon import tables

from openstack_dashboard import api
from openstack_dashboard.dashboards.mydashboard.mypanel import constants

LOG = logging.getLogger(__name__)

class DeletePolicyAction(tables.DeleteAction):
    @staticmethod
    def action_present(count):
        return ungettext_lazy(
            u"Delete Policy",
            u"Delete Policy",
            count
        )

    @staticmethod
    def action_past(count):
        return ungettext_lazy(
            u"Deleted Policy",
            u"Deleted Policy",
            count
        )

    def delete(self, request, obj_id):
        api.nova.policy_delete(request, obj_id)


class CreatePolicyAction(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Policy")
    url = constants.POLICY_CREATE_URL
    classes = ("ajax-modal",)
    icon = "plus"

class PolicyFilterAction(tables.FilterAction):
    def filter(self, table, aggregates, filter_string):
        q = filter_string.lower()

        def comp(aggregate):
            return q in aggregate.name.lower()

        return filter(comp, aggregates)

class UpdatePolicyAction(tables.LinkAction):

    name = "edit"
    verbose_name = _("Edit Policy")
    url = "horizon:mydashboard:policy:update"
    classes = ("ajax-modal",)
    icon = "pencil"



class PolicyTable(tables.DataTable):
    name = tables.Column('name', verbose_name=_('Name'))

    class Meta:
        name = "policy"
        verbose_name = _("Policy")
        table_actions = (PolicyFilterAction,
                         CreatePolicyAction,
                         DeletePolicyAction)
        #should always be row_actions
        row_actions = (UpdatePolicyAction,
                       DeletePolicyAction,
                      )
