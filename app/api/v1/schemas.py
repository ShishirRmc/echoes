from pydantic import BaseModel


class QuoteBase(BaseModel):
    quote: str
    author: str


class Quote(QuoteBase):
    id: int

    model_config = {"from_attributes": True}
