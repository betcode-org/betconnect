from .baseresource import BaseResource


class ResponseMessage(BaseResource):
    message: str
    request_url: str
    status_code: int


class BaseRequestException(BaseResource):
    message: str
    request_url: str
    status_code: int
