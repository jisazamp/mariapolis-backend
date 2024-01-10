from typing import Any, Generic, List, Optional, TypeVar

from pydantic import validator
from pydantic.generics import GenericModel

DataT = TypeVar("DataT")


class Response(GenericModel, Generic[DataT]):
    message: Optional[str]
    status_code: int
    data: Optional[DataT]
    error: Optional[List[Any]]

    @validator("error", always=True)
    def check_consistency(cls, v, values):
        if v is not None and values["status_code"] is None:
            raise ValueError("must provide an status code")
        if v is not None and values["data"] is not None:
            raise ValueError("must not provide both data and error")
        if v is None and values.get("data") is None:
            raise ValueError("must provide data or error")
        return v
