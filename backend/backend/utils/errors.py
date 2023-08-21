from rest_framework.exceptions import ValidationError
from .constants.status_code import StatusCode

class ValidationErrorNew(ValidationError):
    error_code = None
    
    def __init__(self, detail=None, code=None):
        self.error_code = code
        super().__init__(detail, code)
    
    def __get_code(self):
        return self.error_code