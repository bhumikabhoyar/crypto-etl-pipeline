import boto3
import json
import os
import datetime
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def load_to_s3(raw_data):
    try:
        # Convert Timestamps to strings before JSON serialization
        for record in raw_data:
            for key, value in record.items():
                if hasattr(value, 'isoformat'):
                    record[key] = value.isoformat()

        s3 = boto3.client("s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
            aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
            region_name="ap-south-1"
        )
        filename = f"raw/coins_{datetime.date.today()}.json"
        s3.put_object(
            Bucket=os.getenv("S3_BUCKET_NAME"),
            Key=filename,
            Body=json.dumps(raw_data)
        )
        print(f"✅ Uploaded to S3: {filename}")
    except Exception as e:
        print(f"❌ S3 upload failed: {e}")
        raise

def load_to_mysql(df):
    try:
        from urllib.parse import quote_plus
        password = quote_plus(os.getenv('DB_PASSWORD'))
        engine = create_engine(
            f"mysql+pymysql://{os.getenv('DB_USER')}:{password}"
            f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
        )
        df.to_sql("coin_prices", engine, if_exists="append", index=False)
        print(f"✅ Loaded {len(df)} rows to MySQL")
    except Exception as e:
        print(f"❌ MySQL load failed: {e}")
        raise