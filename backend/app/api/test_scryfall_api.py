import pytest
import requests
from unittest.mock import patch

from scryfall_api import get_card_image

# Sample response for mocking Scryfall API response
sample_response = {
    "image_uris": {
        "normal": "https://example.com/card.jpg"
    }
}

# Test case for a successful card lookup without set code
@patch('requests.get')
def test_get_card_image_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = sample_response
    
    card_name = "Black Lotus"
    result = get_card_image(card_name)
    assert result == "https://example.com/card.jpg"

# Test case for a successful card lookup with set code
@patch('requests.get')
def test_get_card_image_with_set_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = sample_response
    
    card_name = "Black Lotus"
    set_code = "lea"
    result = get_card_image(card_name, set_code)
    assert result == "https://example.com/card.jpg"

# Test case for a card not found
@patch('requests.get')
def test_get_card_image_not_found(mock_get):
    mock_get.return_value.status_code = 404
    
    card_name = "Nonexistent Card"
    result = get_card_image(card_name)
    assert result == "Card not found"