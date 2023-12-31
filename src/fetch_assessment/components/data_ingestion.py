import os
import urllib.request as request
from fetch_assessment.logging import logger
from fetch_assessment.utils.common import get_size
from pathlib import Path
from fetch_assessment.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            try:
                filename, headers = request.urlretrieve(
                    url = self.config.source_URL,
                    filename = self.config.local_data_file
                )
            except Exception as e:
                print("Could not download from the link using the alternative link ...")
                filename, headers = request.urlretrieve(
                    url = self.config.alt_source_URL,
                    filename = self.config.local_data_file
                )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

        