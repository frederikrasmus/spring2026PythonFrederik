import os

from dotenv import load_dotenv

# load_dotenv() returnerer True hvis den finder en fil
found = load_dotenv() 

print(f"Fandt .env filen? {found}")
print(f"API_KEY: {os.getenv('API_KEY')}")