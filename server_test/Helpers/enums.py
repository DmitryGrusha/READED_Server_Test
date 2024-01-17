from enum import Enum


class ResponseType(Enum):
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"

    def __str__(self):
        return self.value
