from fastapi.testclient import TestClient
from app.main import app
from app.api.v1.schemas import Quote
from app.services.quote_service import _load_quotes # For checking against loaded data

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

def test_get_random_quote():
    response = client.get("/api/v1/quote")
    assert response.status_code == 200
    quote_data = response.json()
    assert "quote" in quote_data
    assert "author" in quote_data
    # Check if the returned quote is one of the loaded quotes
    loaded_quotes = [q.model_dump() for q in _load_quotes()]
    assert quote_data in loaded_quotes

def test_get_all_quotes():
    response = client.get("/api/v1/quotes")
    assert response.status_code == 200
    quotes_list = response.json()
    assert isinstance(quotes_list, list)
    loaded_quotes = [q.model_dump() for q in _load_quotes()]
    assert len(quotes_list) == len(loaded_quotes)
    for quote_data in quotes_list:
        assert quote_data in loaded_quotes
