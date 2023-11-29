from QSARFishToxicity.config.configuration import ConfigurationManager
from QSARFishToxicity.components.data_base_ops_training import DataBaseOperations
from QSARFishToxicity.components.data_transformation import DataTransformationTraining


class DatabaseOperationsTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_base_operations_training_config = config.get_data_base_operations_trainig_config()
        data_base_operations_training_credentials = config.get_data_base_operations_training_credentials()
        data_base_operations_training_params = config.get_data_base_operations_training_params()
        data_base_training = DataBaseOperations(config=data_base_operations_training_config,
                                                credentials=data_base_operations_training_credentials,
                                                params=data_base_operations_training_params,)
        data_base_training.create_table_db()
        data_base_training.insert_into_table_good_data()

        data_transformation_training_config = config.get_data_transformation_training_config()
        data_transformation_training = DataTransformationTraining(config=data_transformation_training_config)
        data_transformation_training.delete_existing_good_data_training_folder()
        data_transformation_training.move_bad_files_to_archive_bad()

        data_base_training.export_data_from_table_into_csv()