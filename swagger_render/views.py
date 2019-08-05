from django.views.generic import TemplateView
from django.conf import settings

from swagger_render.exceptions import IndexFileNotSetException


class SwaggerUIView(TemplateView):
    template_name = 'swagger_render/index.html'

    def get(self, request, *args, **kwargs):
        try:
            index_filename = getattr(settings, 'SWAGGER_YAML_FILENAME')
        except AttributeError:
            raise IndexFileNotSetException('You did not add SWAGGER_YAML_FILENAME into your settings file')

        return self.render_to_response({'url': index_filename})
