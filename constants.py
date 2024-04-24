from pathlib import Path


ASSETS_DIR = Path("./assets")
DATA_DIR = ASSETS_DIR / "data"
HOTELS_DATA = DATA_DIR / "hotels.csv"
CARDS_DATA = DATA_DIR / "cards.csv"
CARDS_SECURITY_DATA = DATA_DIR / "card_security.csv"
RECEIPT_DIR = ASSETS_DIR / "receipts"

# Validation patterns
HOTEL_ID_PATTERN = r'^\d{3}$'
# for name pattern allow alphabetical characters with 1 space betwen like 'John Doe'
NAME_PATTERN = r'^[a-zA-Z]+ [a-zA-Z]+$'
CARD_NUMBER_PATTERN = r'^\d{16}$'
EXPIRATION_PATTERN = r'^\d{2}/\d{2}$'
CVC_PATTERN = r'^\d{3}$'
CARD_AUTH_PATTERN = r'^\S{6,}$'  # `\S` matches any non-whitespace character.
