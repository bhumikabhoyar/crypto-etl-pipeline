# Crypto ETL Pipeline

Automated ETL pipeline that extracts live cryptocurrency data 
from CoinGecko API, transforms it with Pandas, stores raw JSON 
to AWS S3, and loads clean data into MySQL for Tableau visualization.

## Tech Stack
Python | Pandas | AWS S3 | MySQL | Tableau | Docker

## Setup
1. Clone the repo
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Add your credentials to `.env`
6. Run: `python etl.py`
mysql -u root -p
## Project Structure
- `extract.py` — pulls data from CoinGecko API
- `transform.py` — cleans and shapes data with Pandas
- `load.py` — uploads to AWS S3 and MySQL
- `etl.py` — orchestrates the full pipeline
- `Dockerfile` — containerizes the pipeline