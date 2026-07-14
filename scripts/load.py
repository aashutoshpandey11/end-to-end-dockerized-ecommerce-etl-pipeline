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

    engine = create_engine(
        "postgresql://postgres:postgresql@postgres:5432/ecommerce_db"
    )

    df.to_sql(
        "products",
        engine,
        if_exists="replace",
        index=False
    )

    logger.info("Data loaded successfully.")