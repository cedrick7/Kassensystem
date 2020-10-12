from django_filters import filters

__all__ = (
    'OrderingFilter',
)


class OrderingFilter(filters.OrderingFilter):
    def __init__(self, *args, **kwargs):
        self.field_cases = kwargs.pop('field_cases', {})
        super().__init__(*args, **kwargs)

    def get_ordering_value(self, param):
        descending = param.startswith('-')
        param = param[1:] if descending else param
        field_name = self.param_map.get(param, param)
        field_case = self.field_cases.get(field_name)
        if field_case:
            return field_case(field_name).desc() if descending else field_case(field_name)
        return '-%s' % field_name if descending else field_name
