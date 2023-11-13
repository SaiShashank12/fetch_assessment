from fetch_assessment.config.configuration import ConfigurationManager
from fetch_assessment.components.training_model import ModelTrainer
from fetch_assessment.logging import logger

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_training_model_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.training()