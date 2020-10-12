# django-filter-addons [![Build Status](https://travis-ci.org/xavierdutreilh/django-filter-addons.svg?branch=master)](https://travis-ci.org/xavierdutreilh/django-filter-addons)

> A collection of addons for [django-filter](https://github.com/carltongibson/django-filter)

## Installation

Install the package from PyPi:

```bash
pip install django-filter-addons
```

## Usage

Implement case-insensitivity on queryset ordering:

```python
from django.contrib.auth.models import User
from django.db.models.functions import Lower

from django_filters.filters import CharFilter
from django_filters.filterset import FilterSet

from django_filters_addons.filters import OrderingFilter

class UserFilter(FilterSet):
    account = CharFilter(field_name='username')
    sort = OrderingFilter(
        fields={'username': 'account', 'first_name': 'first_name', 'last_name': 'last_name', 'email': 'email'},
        field_cases={'username': Lower, 'email': Lower},
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
```

## License

`django-filter-addons` is released under the [MIT license](http://en.wikipedia.org/wiki/MIT_License).


