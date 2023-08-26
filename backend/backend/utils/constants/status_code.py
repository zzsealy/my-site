from enum import Enum

class StatusCode(Enum):
    OK = 200 
    PASS_NOT_EQUAL = 4001
    ERROR = 400
    EMAIL_EXIST = 4002
    PASSWORD_ERROR = 4003
    USER_NOT_EXIST = 4004