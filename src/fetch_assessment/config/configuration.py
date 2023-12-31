from fetch_assessment.constants import *
from fetch_assessment.utils.common import read_yaml, create_directories
from fetch_assessment.entity import (DataIngestionConfig,FeatureengineeringConfig,SplitingDataConfig,TrainingModelConfig,EvaluatingModelConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
        

    

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            alt_source_URL=config.alt_source_URL 
        )

        return data_ingestion_config
    
    def get_data_transformation_config(self) -> FeatureengineeringConfig:
        config = self.config.feature_engineering

        create_directories([config.root_dir])

        feature_eng_config = FeatureengineeringConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            #tokenizer_name = config.tokenizer_name
        )

        return feature_eng_config

    def get_Spliting_Data_config(self) -> SplitingDataConfig:
        config = self.config.spliting_data
        params = self.params.splitingparameters
        create_directories([config.root_dir])

        spliting_data_config = SplitingDataConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            look_back=params.look_back,
            split=params.split
        )

        return spliting_data_config
    
    def get_training_model_config(self) -> TrainingModelConfig:
        config = self.config.model_training
        params=self.params.TrainingArguments
        create_directories([config.root_dir])

        traing_model_config = TrainingModelConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path=config.model_path,
            epoch=params.epoch,
            batch_size=params.batch_size,
            look_back=params.look_back            
                    )

        return traing_model_config
    
    def get_evaluating_model_config(self) ->  EvaluatingModelConfig:
        config = self.config.model_evaluating
        create_directories([config.root_dir])

        traing_model_config =  EvaluatingModelConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path=config.model_path,
                    )

        return traing_model_config