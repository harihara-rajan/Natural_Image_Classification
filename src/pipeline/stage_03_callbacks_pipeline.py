import os 
from src.config.configuration_manager import ConfigurationManager
from src.components.stage_03_callbacks import CALLBACKSCOMPONENT
from __init__ import params_path , config_path
from utils.common import read_yaml

class CallBacksPipeline():
    """
    CallBacksPipeline is a class designed for managing and executing a pipeline of callbacks for a deep learning model
    training process. It reads parameters and configuration from YAML files, creates a `CALLBACKSCOMPONENT` instance,
    and retrieves a list of callbacks to be used during training.

    Attributes:
        params (dict): Dictionary containing parameters for the callback pipeline.
        config (dict): Dictionary containing configuration settings for the callback pipeline.

    Methods:
        __init__(self, params_path: str = params_path, config_path: str = config_path): Constructor method
            to initialize the CallBacksPipeline with the paths to the parameters and configuration YAML files.
        main(self): Main method to execute the callback pipeline, including the creation of CALLBACKSCOMPONENT instance
            and retrieval of the callbacks list.

    Example Usage:
        # Instantiate CallBacksPipeline with paths to parameters and configuration YAML files
        pipeline = CallBacksPipeline(params_path='path/to/params.yaml', config_path='path/to/config.yaml')

        # Execute the callback pipeline
        pipeline.main()
    """
    def __init__(self, params_path = params_path, config_path=config_path):
        """
        Initializes the CallBacksPipeline with the paths to parameters and configuration YAML files.

        Args:
            params_path (str): Path to the YAML file containing parameters for the callback pipeline.
            config_path (str): Path to the YAML file containing configuration settings for the callback pipeline.
        """
        self.params = read_yaml(params_path)
        self.config = read_yaml(config_path)
    
    def main():
        """
        Main method to execute the callback pipeline, including the creation of CALLBACKSCOMPONENT instance
        and retrieval of the callbacks list.
        """
        cm = ConfigurationManager()
        callbacksentity = cm.get_callbacks_entity()
        callbacks_component = CALLBACKSCOMPONENT(callbacksentity)
        callbacks_component.callbacks_list()
    