import os 
from src.config.configuration_manager import ConfigurationManager
from src.components.stage_03_callbacks import CALLBACKSCOMPONENT
from src.components.stage_04_model_training import TrainingComponent
from __init__ import config_path, params_path
from src.utils.common import read_yaml

class ModelTrainingPipeline():
    def __init__(self, params_path = config_path, config_path=params_path):
        self.params = read_yaml(params_path)
        self.config = read_yaml(config_path)
    
    def main():
        cm = ConfigurationManager()
        callbacksentity = cm.get_callbacks_entity()
        callbacks_component = CALLBACKSCOMPONENT(callbacksentity)
        callback = callbacks_component.callbacks_list()

        training_entity = cm.get_training_entity()
        training_component = TrainingComponent(TrainingEntity= training_entity)
        training_component.test_train_split()
        training_component.train(callback_list=callback)
    