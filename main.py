from fetch_assessment.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from fetch_assessment.pipeline.stage_02_feature_engineering import FeatureengineeringPipeline
from fetch_assessment.pipeline.stage_03_spliting_data import SplitingPipeline
from fetch_assessment.pipeline.stage_04_training_model import ModelTrainingPipeline
from fetch_assessment.pipeline.stage_05_Evaluating_model import ModelEvaluatingPipeline

from fetch_assessment.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Feature Engineering stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   Feature_Engineering = FeatureengineeringPipeline()
   Feature_Engineering.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Spliting stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   Spliting_Data = SplitingPipeline()
   Spliting_Data.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Training stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   ModelTraining = ModelTrainingPipeline()
   ModelTraining.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Evaluating stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   ModelTraining =ModelEvaluatingPipeline() 
   ModelTraining.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e