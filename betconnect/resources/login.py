from .baseresource import BaseResource
from pydantic import BaseModel, Field, validator
from typing import List
from datetime import datetime


class Token(BaseResource):
    token: str


class Login(BaseResource):
    message: str
    data: Token
