from fetch_assessment.config.configuration import ConfigurationManager
from fetch_assessment.components.feature_egineering import Featureengineering
from fetch_assessment.logging import logger

class FeatureengineeringPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        Feature_engineering_config = config.get_data_transformation_config()
        data_transformation = Featureengineering(config=Feature_engineering_config)
        data_transformation.features()