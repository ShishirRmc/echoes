import json
import random
from typing import List, Optional
from app.api.v1.schemas import Quote
from app.core.config import settings
import os

_quotes_cache: Optional[List[Quote]] = None

def _load_quotes() -> List[Quote]:
    global _quotes_cache
    if _quotes_cache is None:
        quotes_path = settings.QUOTES_FILE_PATH
        if not os.path.exists(quotes_path):
            # Fallback if file doesn't exist or path is incorrect
            # This could be logged or handled more gracefully
            _quotes_cache = [
                Quote(id=0, quote="Default quote: Be the change you wish to see.", author="Mahatma Gandhi")
            ]
            return _quotes_cache
        try:
            with open(quotes_path, "r") as f:
                quotes_data = json.load(f)
            _quotes_cache = [Quote(**q) for q in quotes_data]
        except (json.JSONDecodeError, FileNotFoundError) as e:
            # Log error e
            _quotes_cache = [
                Quote(id=0, quote="Error loading quotes. Please check configuration.", author="System")
            ]
    return _quotes_cache

def get_random_quote() -> Quote:
    quotes = _load_quotes()
    if not quotes:
         # Should not happen if fallback is in _load_quotes
        return Quote(id=-1, quote="No quotes available.", author="System")
    return random.choice(quotes)

def get_all_quotes() -> List[Quote]:
    return _load_quotes()
