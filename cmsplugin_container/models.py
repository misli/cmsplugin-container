# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

from cms.models import CMSPlugin
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


CONTAINER_TEMPLATES = getattr(settings, 'CONTAINER_TEMPLATES', {
    'container': _('container'),
    'carousel': _('carousel'),
})


@python_2_unicode_compatible
class ContainerPlugin(CMSPlugin):
    template = models.CharField('template', max_length=50, choices = CONTAINER_TEMPLATES.items())

    def __str__(self):
        return '{}'.format(CONTAINER_TEMPLATES[self.template])

