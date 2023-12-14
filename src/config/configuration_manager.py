from __init__  import config_path, params_path
from src.entity.entity_config import (ConfigDataIngest, 
                                      ConfigPreprocess)
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
    
    def get_preprocess_config(self)->ConfigPreprocess:
        """
        method is used to get the configuration for the 
        "image preprocessing stage" : second stage in the ML pipeline 
        """
        preprocess_config = ConfigPreprocess(
            data_folder=self.config.Preprocess, 
            Augmentation= self.params.Augmentation,
            Image_Size= self.params.Image_Size
        )

        return preprocess_config

