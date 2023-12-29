import os
from src.config.configuration_manager import ConfigurationManager
from src.components.stage_02_base_model_generator import BaseModelGeneratorComponent
from __init__ import config_path, params_path
from src.utils.common import read_yaml
class BaseModelPipeline:
    def __init__(self, params_path = params_path, config_path=config_path):
        self.params = read_yaml(params_path)
        self.config = read_yaml(config_path)
    def main(self):
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