# Django Swagger Render

## Getting Started

### Prerequisites

- python >= 3.5
- Django >= 2.0

### Installation

Install using pip

```
pip install django-swagger-render
```

Add 'swagger_render' to your INSTALLED_APPS setting.

```
INSTALLED_APPS = [
    ...
    'swagger_render',
]
```

Create the folder where you will store your documentation

```
mkdir docs
```

Create the `index.yml` file with some `OPENAPI` or `Swagger` specifications

```
touch docs/index.yml
```

Serve your documentation files
```
urlpatterns += static('/docs/', document_root='docs')
```

Add `SWAGGER_YAML_FILENAME` setting to your `settings.py`

```
SWAGGER_YAML_FILENAME = '/docs/index.yml'
```

Add the `SwaggerUIView` to your urls

```
from swagger_render.views import SwaggerUIView


urlpatterns = [
    ...
    path('swagger/', SwaggerUIView.as_view()),
]
```

Voila!
