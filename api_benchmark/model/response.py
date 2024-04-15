from pydantic import BaseModel


class ArrayValueResponse(BaseModel):
    value: int | float


class ErrorResponse(BaseModel):
    reason: str
