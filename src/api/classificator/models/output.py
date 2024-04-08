from pydantic import BaseModel


class OutputModel(BaseModel):
    product: str
    quantity: int
    type: str
