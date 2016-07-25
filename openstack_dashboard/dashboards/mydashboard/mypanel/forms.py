import logging
import json

from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms
from horizon import messages

from openstack_dashboard import api

LOG = logging.getLogger(__name__)



'''
class CreatePolicyForm(forms.SelfHandlingForm):

    #Add attributes refer to tables.py
    #name = forms.CharField(max_length=255, label=_("Name"))

    def __init__(self, request, *args, **kwargs):
        super(CreatePolicyForm, self).__init__(request, *args, **kwargs)
    def clean(self):
        data = super(CreatePolicyForm, self).clean()

        return data
    def handle(self, request, data):
        # Glance does not really do anything with container_format at the
        # moment. It requires it is set to the same disk_format for the three
        # Amazon image types, otherwise it just treats them as 'bare.' As such
        # we will just set that to be that here instead of bothering the user
        # with asking them for information we can already determine.

        #Add attributes as above
        meta = {
                #'name': data['name']
                }

        try:
            api.nova.Policy_create(
                request,
                **meta)
        except Exception:
            exceptions.handle(request, _('Unable to create Policy.'))
            return False
        return True

class UpdatePolicyForm(forms.SelfHandlingForm):

    #Add attributes you want to update
    #name = forms.CharField(label=_("Name"),
    #                       max_length=255)

    def __init__(self, request, *args, **kwargs):
        super(UpdatePolicyForm, self).__init__(request, *args, **kwargs)

    def handle(self, request, data):
        id = self.initial['id']


        #add your own attributes
        #name = data['name']
        #policy = {'name': name}


        try:
            api.nova.Policy_update(request, id, policy)
            message = _('Successfully updated aggregate: "%s."') \
                      % data['name']
            messages.success(request, message)
        except Exception:
            exceptions.handle(request,
                              _('Unable to update the aggregate.'))
        return True

'''
