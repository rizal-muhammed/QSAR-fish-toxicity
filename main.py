from QSARFishToxicity.logging import logger
from QSARFishToxicity.pipeline.stage_01_data_ingestion import DataIngestionPipeline


STAGE_NAME = f"""Data Ingestion"""
try:
    logger.info(f""">>>>>>> Stage {STAGE_NAME} started... <<<<<<<""")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f""">>>>>>> Stage {STAGE_NAME} Completed... <<<<<<<\n\n""")
except Exception as e:
    logger.exception(e)
    raise e