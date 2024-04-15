from pydantic import BaseModel


class GetValueRequest(BaseModel):
    row: int
    column: int
    multiplier: int | float | None = None
