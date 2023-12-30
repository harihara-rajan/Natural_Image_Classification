import os
from src.config.configuration_manager import ConfigurationManager
from src.components.stage_02_base_model_generator import BaseModelGeneratorComponent
from __init__ import config_path, params_path
from src.utils.common import read_yaml
class BaseModelPipeline:
    """
    BaseModelPipeline is a class designed to streamline the process of generating a base and actual deep learning model.
    It reads parameters and configuration from YAML files using the ConfigurationManager,
    instantiates the BaseModelGeneratorComponent, and executes the base model generation pipeline.

    Attributes:
        params (dict): Dictionary containing parameters for the base model generation pipeline.
        config (dict): Dictionary containing configuration settings for the base model generation pipeline.

    Methods:
        __init__(self, params_path=params_path, config_path=config_path): Constructor method
            to initialize the BaseModelPipeline with paths to the parameters and configuration YAML files.
        main(self): Main method to execute the base model generation pipeline.

    Example Usage:
        # Instantiate BaseModelPipeline with paths to parameters and configuration YAML files
        base_model_pipeline = BaseModelPipeline(params_path='path/to/params.yaml', config_path='path/to/config.yaml')

        # Execute the base model generation pipeline
        base_model_pipeline.main()
    """
    def __init__(self, params_path = params_path, config_path=config_path):
        """
        Initializes the BaseModelPipeline with paths to parameters and configuration YAML files.

        Args:
            params_path (str): Path to the YAML file containing parameters for the base model generation pipeline.
            config_path (str): Path to the YAML file containing configuration settings for the base model generation pipeline.
        """
        self.params = read_yaml(params_path)
        self.config = read_yaml(config_path)
    def main(self):
        """
        Main method to execute the base model generation pipeline.
        Instantiates BaseModelGeneratorComponent and executes the base model generation process.
        """
        cm = ConfigurationManager()
        base_model_entity = cm.get_base_model_generator_entity()
        base_model_componet = BaseModelGeneratorComponent(base_model_entity)
        base_model = base_model_componet.load_base_model()
        am = base_model_componet.actual_model(classes=self.params.CLASSES,
            freeze_all=True,
            freeze_till=0,
            learning_rate=self.params.LR)

if __name__ == "__main__":
    A = BaseModelPipeline
    A.main()