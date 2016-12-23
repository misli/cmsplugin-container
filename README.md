# cmsplugin-container
Simple django CMS plugin to render sub-plugins in different templates

## configuration

Add ```'cmsplugin_container'``` to ```INSTALLED_APPS```.

You may want to override the ```CONTAINER_TEMPLATES``` setting.
The default value is following:

```python
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
```

See [container.html](cmsplugin_container/templates/container/container.html)
for very basic example wrapping sub-plugins into ```<div>``` with configured class.
See [carousel.html](cmsplugin_container/templates/container/carousel.html)
for more complex example.
