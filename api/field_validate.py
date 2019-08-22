from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
import ast


@deconstructible
class FieldsValidator():
    error_code = 'Invalid parameter'
    error_message = _('Can not parse text as JSON')

    def __call__(self, value):
        try:
            tmp = ast.literal_eval(value)
        except:
            tmp = None
        if not isinstance(tmp, dict):
            raise ValidationError(
                self.error_message,
                code=self.error_code
            )
