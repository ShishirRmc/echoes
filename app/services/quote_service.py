import json
import logging
import os
import random
from typing import List, Optional

from app.api.v1.schemas import Quote
from app.core.config import settings

_quotes_cache: Optional[List[Quote]] = None


def _load_quotes() -> List[Quote]:
    global _quotes_cache
    if _quotes_cache is None:
        quotes_path = settings.QUOTES_FILE_PATH
        logger = logging.getLogger(__name__)
        logger.info(f"Attempting to load quotes from: {quotes_path}")
        if not os.path.exists(quotes_path):
            logger.error(f"Quotes file not found at: {quotes_path}")
            # Fallback if file doesn't exist or path is incorrect
            # This could be logged or handled more gracefully
            _quotes_cache = [
                Quote(
                    id=0,
                    quote="Default quote: Be the change you wish to see.",
                    author="Mahatma Gandhi",
                )
            ]
            return _quotes_cache
        try:
            with open(quotes_path, "r") as f:
                quotes_data = json.load(f)
            _quotes_cache = [Quote(**q) for q in quotes_data]
        except (json.JSONDecodeError, FileNotFoundError) as e:
            logger = logging.getLogger(__name__)
            logger.error(f"Error loading quotes: {str(e)}")
            _quotes_cache = [
                Quote(
                    id=0,
                    quote="Error loading quotes. Please check configuration.",
                    author="System",
                )
            ]
    return _quotes_cache


def get_random_quote() -> Quote:
    """
    Get a random quote from the collection.
    Returns a default quote if no quotes are available.
    """
    quotes = _load_quotes()
    return random.choice(quotes)


def get_all_quotes() -> List[Quote]:
    """
    Get all available quotes.
    Returns:
        List[Quote]: List of all quotes
    """
    return _load_quotes()
