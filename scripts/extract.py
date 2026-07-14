import requests
import pandas as pd

from utils.logger import logger


def extract_data():
    """
    Extract product data from Fake Store API.
    """

    logger.info("=" * 50)
    logger.info("Starting Extraction")

    url = "https://fakestoreapi.com/products"

    try:

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        df = pd.DataFrame(data)

        df.to_csv(
            "data/raw/products.csv",
            index=False
        )

        logger.info(f"Downloaded {len(df)} products.")
        logger.info("Raw data saved to data/raw/products.csv")

    except Exception as e:
        logger.exception(f"Extraction Failed : {e}")
        raise