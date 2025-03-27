import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Ambil variabel dari .env
BOT_TOKEN = os.getenv("BOT_TOKEN")
