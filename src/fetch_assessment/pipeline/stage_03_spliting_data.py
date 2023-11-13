from fetch_assessment.config.configuration import ConfigurationManager
from fetch_assessment.components.spliting_data import Spliting_Data
from fetch_assessment.logging import logger

class SplitingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        Split_Data_config = config.get_Spliting_Data_config()
        Split_Data = Spliting_Data(config=Split_Data_config)
        Split_Data.saving_data()