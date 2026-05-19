import os
from dotenv import load_dotenv
from quantvn.vn.data.utils import client

load_dotenv()

api_key = os.getenv("QUANTVN_API")

if not api_key:
    raise ValueError("Không tìm thấy QUANTVN_API_KEY trong file .env")

client(apikey=api_key)