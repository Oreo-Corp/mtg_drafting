import requests
import sys

def get_card_image(card_name, set_code=None):
    base_url = "https://api.scryfall.com/cards/named"
    params = {"exact": card_name}
    
    if set_code:
        # If there's a set specified, return the image for that set
        params["set"] = set_code
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        card_data = response.json()
        return card_data['image_uris']['normal']
    else:
        return "Card not found"

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python scryfall_api.py <card_name> [set_code]")
        sys.exit(1)
    
    card_name = sys.argv[1]
    set_code = sys.argv[2] if len(sys.argv) == 3 else None
    
    card_image_url = get_card_image(card_name, set_code)
    
    if card_image_url != "Card not found":
        print(f"Image URL for {card_name}: {card_image_url}")
    else:
        print("Card not found")