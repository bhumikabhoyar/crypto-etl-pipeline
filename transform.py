import pandas as pd

def transform(df):
    df = df[["id","symbol","name","current_price",
             "market_cap","total_volume",
             "price_change_percentage_24h","extracted_at"]]
    df.columns = ["coin_id","symbol","name","price_inr",
                  "market_cap","volume_24h",
                  "price_change_pct","extracted_at"]
    df.dropna(inplace=True)
    df["price_change_pct"] = df["price_change_pct"].round(2)
    print(f"✅ Transformed {len(df)} records")
    return df