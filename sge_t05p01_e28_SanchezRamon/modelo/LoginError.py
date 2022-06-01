from enum import IntEnum, unique

@unique
class LoginError(IntEnum):
    USER_ERROR = 1
    PASSWORD_ERROR = 2
    PERMISSION_ERROR = 3
    NO_ERROR = 0