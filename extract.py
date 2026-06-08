import requests
import pandas as pd
import datetime

def extract():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {"vs_currency": "inr", "order": "market_cap_desc", "per_page": 50}
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        df = pd.DataFrame(response.json())
        df["extracted_at"] = datetime.datetime.now()
        print(f"✅ Extracted {len(df)} records")
        return df
    except Exception as e:
        print(f"❌ Extraction failed: {e}")
        raise