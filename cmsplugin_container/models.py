from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

from cms.models import CMSPlugin
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


CONTAINER_TEMPLATES = getattr(settings, 'CONTAINER_TEMPLATES', {
    'container': {
        'label':    _('container'),
        'template': 'container',
        'context':  {'class': 'container'},
    },
    'carousel': {
        'label':    _('carousel'),
        'template': 'carousel',
        'context':  {},
    },
})



def get_label(key):
    try:
        return CONTAINER_TEMPLATES[key]['label']
    except TypeError:
        return CONTAINER_TEMPLATES[key]


CONTAINER_TEMPLATES_CHOICES = [ (key, get_label(key)) for key in CONTAINER_TEMPLATES ]


@python_2_unicode_compatible
class ContainerPlugin(CMSPlugin):
    template = models.CharField('template', max_length=50, choices = CONTAINER_TEMPLATES_CHOICES)

    def get_template(self):
        try:
            return CONTAINER_TEMPLATES[self.template]['template']
        except TypeError:
            return self.template

    @property
    def context(self):
        try:
            return CONTAINER_TEMPLATES[self.template]['context'] or {}
        except TypeError:
            return {}

    def __str__(self):
        return '{}'.format(get_label(self.template))

