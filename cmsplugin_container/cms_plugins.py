from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import ContainerPlugin


@plugin_pool.register_plugin
class ContainerPlugin(CMSPluginBase):
    model = ContainerPlugin
    name = _('Container')
    text_enabled = True
    allow_children = True

    def get_render_template(self, context, instance, placeholder):
        return 'container/%s.html' % instance.get_template()


