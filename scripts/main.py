import time

from utils.logger import logger

from extract import extract_data
from transform import transform_data
from load import load_data


def main():

    start = time.time()

    logger.info("=" * 60)
    logger.info("E-Commerce ETL Pipeline Started")
    logger.info("=" * 60)

    try:

        extract_data()

        transform_data()

        load_data()

        total_time = round(time.time() - start, 2)

        logger.info("=" * 60)
        logger.info("Pipeline Completed Successfully")
        logger.info(f"Execution Time : {total_time} seconds")
        logger.info("=" * 60)

    except Exception as e:

        logger.exception(f"Pipeline Failed : {e}")


if __name__ == "__main__":
    main()