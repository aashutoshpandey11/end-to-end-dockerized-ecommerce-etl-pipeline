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
        "postgresql://l6UxY36EQoS6zFnlr5IuYPdxdl3SPJ9x@dpg-d9biutok1i2s73dq4fc0-a.oregon-postgres.render.com:5432/ecommerce_db_7pdg"
    )

    df.to_sql(
        "products",
        engine,
        if_exists="replace",
        index=False
    )

    logger.info("Data loaded successfully.")