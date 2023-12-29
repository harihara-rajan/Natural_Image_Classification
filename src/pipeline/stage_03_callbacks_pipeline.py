import os 
from config.configuration import ConfigurationManager
from components.stage_03_callbacks import CALLBACKSCOMPONENT
from constants.__init__ import PARAMS_FILE_PATH, CONFIG_FILE_PATH
from utils.common import read_yaml

class CallBacksPipeline():
    def __init__(self, params_path = PARAMS_FILE_PATH, config_path=CONFIG_FILE_PATH):
        self.params = read_yaml(params_path)
        self.config = read_yaml(config_path)
    
    def main():
        cm = ConfigurationManager()
        callbacksentity = cm.get_callbacks_entity()
        callbacks_component = CALLBACKSCOMPONENT(callbacksentity)
        callbacks_component.callbacks_list()
    