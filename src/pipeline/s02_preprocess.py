from src.config.configuration_manager import ConfigurationManager
from src.components.preprocess_components import PreprocessComponent
class PreprocessPipeline:
    def __init__(self):
        pass
    def main(self):
        cm_preprocess = ConfigurationManager()
        preprocess_config = cm_preprocess.get_preprocess_config()
        preprocess_components = PreprocessComponent(preprocess_config)
        train_loader, val_loader = preprocess_components.preprocess_data()
