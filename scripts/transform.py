import ast
import pandas as pd

from utils.logger import logger


def transform_data():
    """
    Clean and transform product data.
    """

    logger.info("=" * 50)
    logger.info("Starting Transformation")

    df = pd.read_csv("data/raw/products.csv")

    logger.info(f"Rows before cleaning : {len(df)}")

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Remove missing values
    df.dropna(inplace=True)

    logger.info(f"Rows after cleaning : {len(df)}")

    # Rename column
    df.rename(
        columns={
            "price": "product_price"
        },
        inplace=True
    )

    # Convert rating string to dictionary
    df["rating"] = df["rating"].apply(ast.literal_eval)

    # Split rating
    df["rating_count"] = df["rating"].apply(lambda x: x["count"])
    df["rating"] = df["rating"].apply(lambda x: x["rate"])

    # Discount
    df["discount_price"] = df["product_price"] * 0.90

    # Data Quality Validation
    assert df["product_price"].isnull().sum() == 0
    assert (df["product_price"] > 0).all()
    assert (df["rating"] >= 0).all()

    logger.info("Data quality validation passed.")

    df.to_csv(
        "data/cleaned/cleaned_products.csv",
        index=False
    )

    logger.info("Cleaned data saved.")