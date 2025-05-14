from pydantic import BaseModel

class QuoteBase(BaseModel):
    quote: str
    author: str

class Quote(QuoteBase):
    id: int

    class Config:
        from_attributes = True 