from QSARFishToxicity.logging import logger
from QSARFishToxicity.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from QSARFishToxicity.pipeline.stage_02_data_validation_training import DataValidationTrainingPipeline


# STAGE_NAME = f"""Data Ingestion"""
# try:
#     logger.info(f""">>>>>>> Stage {STAGE_NAME} started... <<<<<<<""")
#     data_ingestion = DataIngestionPipeline()
#     data_ingestion.main()
#     logger.info(f""">>>>>>> Stage {STAGE_NAME} Completed... <<<<<<<\n\n""")
# except Exception as e:
#     logger.exception(e)
#     raise e

STAGE_NAME = f"""Data Validation Training"""
try:
    logger.info(f""">>>>>>> Stage {STAGE_NAME} started... <<<<<<<""")
    data_validation_training = DataValidationTrainingPipeline()
    data_validation_training.main()
    logger.info(f""">>>>>>> Stage {STAGE_NAME} Completed... <<<<<<<\n\n""")
except Exception as e:
    logger.exception(e)
    raise e