import os 
from src.config.configuration_manager import ConfigurationManager
from src.components.stage_03_callbacks import CALLBACKSCOMPONENT
from src.components.stage_04_model_training import TrainingComponent
from __init__ import config_path, params_path
from src.utils.common import read_yaml

class ModelTrainingPipeline():
    """
    ModelTrainingPipeline is a class designed to streamline the process of training a deep learning model.
    It reads parameters and configuration from YAML files using the ConfigurationManager,
    instantiates the CALLBACKSCOMPONENT and TrainingComponent, and executes the training pipeline.

    Attributes:
        params (dict): Dictionary containing parameters for the model training pipeline.
        config (dict): Dictionary containing configuration settings for the model training pipeline.

    Methods:
        __init__(self, params_path=config_path, config_path=params_path): Constructor method
            to initialize the ModelTrainingPipeline with paths to the parameters and configuration YAML files.
        main(self): Main method to execute the model training pipeline.

    Example Usage:
        # Instantiate ModelTrainingPipeline with paths to parameters and configuration YAML files
        training_pipeline = ModelTrainingPipeline(params_path='path/to/params.yaml', config_path='path/to/config.yaml')

        # Execute the model training pipeline
        training_pipeline.main()
    """
    def __init__(self, params_path = config_path, config_path=params_path):
        """
        Initializes the ModelTrainingPipeline with paths to parameters and configuration YAML files.

        Args:
            params_path (str): Path to the YAML file containing parameters for the model training pipeline.
            config_path (str): Path to the YAML file containing configuration settings for the model training pipeline.
        """
        self.params = read_yaml(params_path)
        self.config = read_yaml(config_path)
    
    def main():
        """
        Main method to execute the model training pipeline.
        Instantiates CALLBACKSCOMPONENT, TrainingComponent, and executes the training pipeline.
        """
        cm = ConfigurationManager()
        callbacksentity = cm.get_callbacks_entity()
        callbacks_component = CALLBACKSCOMPONENT(callbacksentity)
        callback = callbacks_component.callbacks_list()

        training_entity = cm.get_training_entity()
        training_component = TrainingComponent(TrainingEntity= training_entity)
        training_component.test_train_split()
        training_component.train(callback_list=callback)
    