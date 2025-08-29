from datetime import datetime
from typing import Generic, Optional, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


# response schemas
class GenericAPIResponseDetail(BaseModel):
    message: str = Field(default="")
    error_code: str = Field(default="")
    request_id: str


class GenericApiResponse(BaseModel, Generic[T]):
    success: bool = Field(default=True)
    details: GenericAPIResponseDetail = None
    data: Optional[T] = None


class GenericApiResponseWrapper(object):
    def __init__(self, success=True, data=None, detail=None):
        self.success = success
        self.detail = detail
        self.data = data


# Create Event
class CreateEvent(BaseModel):
    name: str
    seats: int


class CreateEventResponse(BaseModel):
    id: int
    name: str
    seats: int


class CreateHoldRequest(BaseModel):
    event_id: int
    qty: int


class BookRequest(BaseModel):
    hold_id: int
    payment_token: str


class CreateHoldResponse(BaseModel):
    id: int
    payment_token: str
    expires_at: datetime


# Get Event
class GetEvent(BaseModel):
    id: int = Optional[None]
