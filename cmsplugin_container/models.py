from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

import warnings

from cms.models import CMSPlugin
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


CONTAINER_TEMPLATES = getattr(settings, 'CONTAINER_TEMPLATES', {
    'container': {
        'label':    _('container'),
        'template': 'container',
        'class':    'container',
    },
    'carousel': {
        'label':    _('carousel'),
        'template': 'carousel',
    },
})



def get_label(key):
    try:
        return CONTAINER_TEMPLATES[key]['label']
    except (TypeError, KeyError):
        warnings.warn('CONTAINER_TEMPLATES should contain dictionaries'
            ' with key "label". Support for old style settings '
            'is deprecated and will be removed in version 1.2',
            DeprecationWarning)
        return CONTAINER_TEMPLATES[key]


CONTAINER_TEMPLATES_CHOICES = [ (key, get_label(key)) for key in CONTAINER_TEMPLATES ]


@python_2_unicode_compatible
class ContainerPlugin(CMSPlugin):
    template = models.CharField('template', max_length=50, choices = CONTAINER_TEMPLATES_CHOICES)

    def get_template(self):
        try:
            return CONTAINER_TEMPLATES[self.template]['template']
        except (TypeError, KeyError):
            return self.template

    @property
    def context(self):
        warnings.warn('ContainerPlugin.context attribute is deprecated '
            'and it will be removed in version 1.2; please use '
            'config attribute instead',
            DeprecationWarning)
        try:
            return CONTAINER_TEMPLATES[self.template]['context'] or {}
        except (TypeError, KeyError):
            return {}

    @property
    def config(self):
        return CONTAINER_TEMPLATES[self.template]

    def __str__(self):
        return '{}'.format(get_label(self.template))

