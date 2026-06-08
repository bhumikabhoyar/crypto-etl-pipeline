from extract import extract
from transform import transform
from load import load_to_s3, load_to_mysql
import logging
import os

# Setup logging
if not os.path.exists("logs"):
    os.makedirs("logs")
logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    print("🚀 Starting ETL Pipeline...")
    logging.info("ETL Pipeline started")

    # Extract
    df = extract()
    raw_data = df.to_dict(orient="records")

    # Transform
    df_clean = transform(df)

    # Load
    load_to_s3(raw_data)
    load_to_mysql(df_clean)

    print("🎉 Pipeline completed successfully!")
    logging.info("ETL Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()