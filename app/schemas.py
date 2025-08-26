from typing import Generic, Optional, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


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
