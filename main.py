from QSARFishToxicity.logging import logger
from QSARFishToxicity.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from QSARFishToxicity.pipeline.stage_02_data_validation_training import DataValidationTrainingPipeline
from QSARFishToxicity.pipeline.stage_03_data_transformation_training import DataTransformationTrainingPipeline
from QSARFishToxicity.pipeline.stage_04_database_ops_training import DatabaseOperationsTrainingPipeline
from QSARFishToxicity.pipeline.stage_05_data_preprocessing_training import DataPreProcessingTrainingPipeline


# STAGE_NAME = f"""Data Ingestion"""
# try:
#     logger.info(f""">>>>>>> Stage {STAGE_NAME} started... <<<<<<<""")
#     data_ingestion = DataIngestionPipeline()
#     data_ingestion.main()
#     logger.info(f""">>>>>>> Stage {STAGE_NAME} Completed... <<<<<<<\n\n""")
# except Exception as e:
#     logger.exception(e)
#     raise e

# STAGE_NAME = f"""Data Validation Training"""
# try:
#     logger.info(f""">>>>>>> Stage {STAGE_NAME} started... <<<<<<<""")
#     data_validation_training = DataValidationTrainingPipeline()
#     data_validation_training.main()
#     logger.info(f""">>>>>>> Stage {STAGE_NAME} Completed... <<<<<<<\n\n""")
# except Exception as e:
#     logger.exception(e)
#     raise e

# STAGE_NAME = f"""Data Transformation Training"""
# try:
#     logger.info(f""">>>>>>> Stage {STAGE_NAME} started... <<<<<<<""")
#     data_transformation_training = DataTransformationTrainingPipeline()
#     data_transformation_training.main()
#     logger.info(f""">>>>>>> Stage {STAGE_NAME} Completed... <<<<<<<\n\n""")
# except Exception as e:
#     logger.exception(e)
#     raise e

# STAGE_NAME = f"""Database Operations Training"""
# try:
#     logger.info(f""">>>>>>> Stage {STAGE_NAME} started... <<<<<<<""")
#     data_insertion_training = DatabaseOperationsTrainingPipeline()
#     data_insertion_training.main()
#     logger.info(f""">>>>>>> Stage {STAGE_NAME} Completed, and data exported as csv for training <<<<<<<\n\n""")
# except Exception as e:
#     logger.exception(e)
#     raise e

STAGE_NAME = f"""Data Pre-Processing Training"""
try:
    logger.info(f""">>>>>>> Stage {STAGE_NAME} started... <<<<<<<""")
    data_preprocessing_training = DataPreProcessingTrainingPipeline()
    data_preprocessing_training.main()
    logger.info(f""">>>>>>> Stage {STAGE_NAME} Completed, and data exported as csv for model building <<<<<<<\n\n""")
except Exception as e:
    logger.exception(e)
    raise e