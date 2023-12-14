from src.pipeline.s01_ingest_data import IngestDataPipeline
from src.logger import logging
stage01 = "Data Ingestion"

logging.info(f"{stage01} Started")
ingest_data = IngestDataPipeline()
ingest_data.main()
logging.info(f"{stage01} Ended")
