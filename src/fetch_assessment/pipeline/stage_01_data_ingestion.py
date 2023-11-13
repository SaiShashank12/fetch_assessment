from fetch_assessment.config.configuration import ConfigurationManager
from fetch_assessment.components.data_ingestion import DataIngestion
from fetch_assessment.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        #data_ingestion.extract_zip_file()