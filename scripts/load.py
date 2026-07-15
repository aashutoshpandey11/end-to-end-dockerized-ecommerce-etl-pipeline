import os
import pandas as pd
from sqlalchemy import create_engine

from utils.logger import logger


def load_data():
    """
    Load cleaned data into PostgreSQL.
    """

    logger.info("=" * 50)
    logger.info("Starting Load")

    df = pd.read_csv(
        "data/cleaned/cleaned_products.csv"
    )

    logger.info(f"Loading {len(df)} records into PostgreSQL")

    DATABASE_URL = os.getenv("DATABASE_URL")

    if not DATABASE_URL:
        raise ValueError("DATABASE_URL environment variable is not set.")

    engine = create_engine(DATABASE_URL)

    df.to_sql(
        "products",
        engine,
        if_exists="replace",
        index=False
    )

    logger.info("Data loaded successfully.")