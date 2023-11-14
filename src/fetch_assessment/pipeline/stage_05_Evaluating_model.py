from fetch_assessment.config.configuration import ConfigurationManager
from fetch_assessment.components.evaluting_model import ModelEvaluator
from fetch_assessment.logging import logger

class ModelEvaluatingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_evaluating_model_config()
        model_evaluator = ModelEvaluator(config=model_trainer_config)
        model_evaluator.evalating()