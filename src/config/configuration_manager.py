from __init__  import config_path, params_path
from src.entity.entity_config import (ConfigDataIngest, 
                                      BaseModelGeneratorEntity,
                                      CALLBACKSENTITY,
                                      TrainingEntity, 
                                      ModelEvaluationEntity)
from src.utils. common import read_yaml

class ConfigurationManager:
    """
    ConfigurationManager is a class designed to manage configurations for different stages in the ML pipeline.
    Each method in the class is responsible for fetching the configuration for a specific ML stage.

    Attributes:
        config_path (str): Path to the YAML file containing general configurations.
        params_path (str): Path to the YAML file containing parameter configurations.

    Methods:
        __init__(self, config_path=config_path, params_path=params_path): Constructor method
            to initialize the ConfigurationManager with paths to the configuration and parameter YAML files.
        get_ingest_data_config(self) -> ConfigDataIngest: Fetches configuration for the "ingest data stage."
        get_base_model_generator_entity(self) -> BaseModelGeneratorEntity: Fetches configuration for the "base model generator stage."
        get_callbacks_entity(self) -> CALLBACKSENTITY: Fetches configuration for callback entities used during training.
        get_training_entity(self) -> TrainingEntity: Fetches configuration for the "model training stage."
        get_model_evaluation_entity(self) -> ModelEvaluationEntity: Fetches configuration for the "model evaluation stage."

    Example Usage:
        # Instantiate ConfigurationManager with paths to configuration and parameter YAML files
        config_manager = ConfigurationManager(config_path='path/to/config.yaml', params_path='path/to/params.yaml')

        # Fetch configuration for the "ingest data stage"
        ingest_data_config = config_manager.get_ingest_data_config()

        # Fetch configuration for the "base model generator stage"
        base_model_entity = config_manager.get_base_model_generator_entity()
    """
    def __init__(self, config_path = config_path, params_path=params_path) -> None:
        """
        Initializes the ConfigurationManager with paths to the configuration and parameter YAML files.

        Args:
            config_path (str): Path to the YAML file containing general configurations.
            params_path (str): Path to the YAML file containing parameter configurations.
        """
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
    
    def get_ingest_data_config(self) -> ConfigDataIngest:
        """
        Fetches configuration for the "ingest data stage."

        Returns:
            ConfigDataIngest: Configuration entity for the "ingest data stage."
        """
        data_ingest_config = ConfigDataIngest(
            data_folder = self.config.Ingest_Data.data_folder,
            dataset_name = self.config.Ingest_Data.dataset_name,
        )

        return data_ingest_config
    
    def get_base_model_generator_entity(self)-> BaseModelGeneratorEntity:
        """
        Fetches configuration for the "base model generator stage."

        Returns:
            BaseModelGeneratorEntity: Configuration entity for the "base model generator stage."
        """
        
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
        """
        Fetches configuration for callback entities used during training.

        Returns:
            CALLBACKSENTITY: Configuration entity for training callbacks.
        """
        config = self.config.prepare_callbacks
        
        callback_entity = CALLBACKSENTITY(root_dir=config.root_dir, 
                                          tensorboard_log_dir=config.tensorboard_log_dir,
                                          checkpoint_file_path=config.checkpoint_file_path
                                          )
        return callback_entity

    def get_training_entity(self)->TrainingEntity:
        """
        Fetches configuration for the "model training stage."

        Returns:
            TrainingEntity: Configuration entity for the "model training stage."
        """
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
        """
        Fetches configuration for the "model evaluation stage."

        Returns:
            ModelEvaluationEntity: Configuration entity for the "model evaluation stage."
        """
        model_evaluation_entity = ModelEvaluationEntity(trained_model_path= self.config.training.trained_model_path,
            training_data_path= self.config.training.training_data_path,
            all_params= self.params,
            params_batch_size= self.params.BATCH_SIZE,
            params_image_size= self.params.IMAGE_SIZE,
            model_no=self.params.MODEL
        )
        return model_evaluation_entity

