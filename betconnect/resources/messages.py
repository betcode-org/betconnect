from .baseresource import BaseResource
from pydantic import Field

class ResponseMessage(BaseResource):
    message: str
    request_url: str
    status_code: int

class BaseRequestException(BaseResource):
    message: str
    request_url: str
    status_code: int
