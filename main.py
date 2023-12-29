from src.pipeline.s01_ingest_data import IngestDataPipeline
from src.pipeline.stage_02_base_model_gen_pipeline import BaseModelPipeline
from src.pipeline.stage_04_model_training_pipeline import ModelTrainingPipeline
from src.pipeline.stage_05_model_evaluation_pipeline import ModelEvaluationPipeline

from src.logger import logging
stage01 = "Data Ingestion"
stage02 = "Base Model Generator"
stage03 = "Model Training"
stage04 = "Model Evaluation"

logging.info(f"{stage01} Started")
ingest_data = IngestDataPipeline()
ingest_data.main()
logging.info(f"{stage01} Ended")

try:
    print(f"Stage 02 {stage02} started")
    model_gen = BaseModelPipeline()
    model_gen.main()
    print(f"Stage 02 {stage02} ended")
except Exception as e:
    raise e

try:
    print(f"Stage 03 {stage03} started")
    callbacks = ModelTrainingPipeline
    callbacks.main()
    print(f"Stage 03 {stage03} ended")
except Exception as e:
    raise e

try:
    print(f"Stage 04 {stage04} started")
    model_eval = ModelEvaluationPipeline
    model_eval.main()
except Exception as e:
    raise e