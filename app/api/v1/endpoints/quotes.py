from typing import List

from fastapi import APIRouter

from app.api.v1 import schemas
from app.services import quote_service

router = APIRouter()


@router.get("/quote", response_model=schemas.Quote)
def read_random_quote():
    """
    Retrieve a random quote.
    """
    return quote_service.get_random_quote()


@router.get("/quotes", response_model=List[schemas.Quote])
def read_all_quotes():
    """
    Retrieve all quotes.
    """
    return quote_service.get_all_quotes()
