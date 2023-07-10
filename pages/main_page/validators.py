from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

MAX_UPLOAD_SIZE = 1048576  # 1 MB


@deconstructible
class MaxUploadSizeValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        if value.size > self.max_size:
            raise ValidationError(f"The maximum file size shouldn't be more than {self.max_size} bytes.")
