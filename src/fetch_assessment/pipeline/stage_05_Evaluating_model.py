from fetch_assessment.config.configuration import ConfigurationManager
from fetch_assessment.components.evaluting_model import ModelEvaluator
from fetch_assessment.logging import logger

class ModelEvaluatingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
            config = ConfigurationManager()
            model_evaluator_config = config.get_evaluating_model_config()
            model_evaluator = ModelEvaluator(config=model_evaluator_config)
            y_train, y_test, y_pred_train, y_pred_test = model_evaluator.evaluating()
            model_evaluator.plot_predictions(y_train, y_pred_train, "train.png")
            model_evaluator.plot_predictions(y_test, y_pred_test, "test.png")