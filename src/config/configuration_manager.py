from __init__  import config_path, params_path
from src.entity.entity_config import (ConfigDataIngest, 
                                      BaseModelGeneratorEntity,
                                      CALLBACKSENTITY,
                                      TrainingEntity, 
                                      ModelEvaluationEntity)
from src.utils. common import read_yaml

class ConfigurationManager:
    """
    for each stages in the ML pipeline, 
    each method in the class is responsible for
    fetching the configuration for the particular
    ML Stage 
    """
    def __init__(self, config_path = config_path, params_path=params_path) -> None:
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
    
    def get_ingest_data_config(self) -> ConfigDataIngest:
        """
        method is used to get the configuration for the 
        "ingest data stage" : first stage in the ML pipeline 
        """
        data_ingest_config = ConfigDataIngest(
            data_folder = self.config.Ingest_Data.data_folder,
            dataset_name = self.config.Ingest_Data.dataset_name,
        )

        return data_ingest_config
    
    def get_base_model_generator_entity(self)-> BaseModelGeneratorEntity:
        
        base_model_entity = BaseModelGeneratorEntity(
            base_model_path  = self.config.base_model_generator.base_model_path,
            actual_model_path= self.config.base_model_generator.actual_model_path,
            CLASSES = self.params.CLASSES,
            EPOCHS = self.params.EPOCHS,
            BATCH_SIZE = self.params.BATCH_SIZE,
            LR = self.params.LR,
            TEST_SIZE = self.params.TEST_SIZE,
            IMAGE_SIZE = self.params.IMAGE_SIZE
        )
        return base_model_entity
    
    def get_callbacks_entity(self)->CALLBACKSENTITY :
        config = self.config.prepare_callbacks
        
        callback_entity = CALLBACKSENTITY(root_dir=config.root_dir, 
                                          tensorboard_log_dir=config.tensorboard_log_dir,
                                          checkpoint_file_path=config.checkpoint_file_path
                                          )
        return callback_entity

    def get_training_entity(self)->TrainingEntity:
        config = self.config.training
        training_entity = TrainingEntity(root_dir=config.root_dir,
                                         actual_model_path=self.config.base_model_generator.actual_model_path,
                                         trained_model_path=config.trained_model_path,
                                         training_data_path=config.training_data_path,
                                         params_epochs= self.params.EPOCHS,
                                         params_batch_size=self.params.BATCH_SIZE,
                                         params_is_augment=self.params.AUG, 
                                         params_image_size=self.params.IMAGE_SIZE,
                                         model_no=self.params.MODEL)
        return training_entity

    def get_model_evaluation_entity(self)->ModelEvaluationEntity:
        model_evaluation_entity = ModelEvaluationEntity(trained_model_path= self.config.training.trained_model_path,
            training_data_path= self.config.training.training_data_path,
            all_params= self.params,
            params_batch_size= self.params.BATCH_SIZE,
            params_image_size= self.params.IMAGE_SIZE,
            model_no=self.params.MODEL
        )
        return model_evaluation_entity

