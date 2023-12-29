from src.config.configuration_manager import ConfigurationManager
from src.components.stage_05_model_evaluation_component import ModelEvaluation
class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def main()->None:
        cm = ConfigurationManager()
        model_eval_entity = cm.get_model_evaluation_entity()
        model_eval_component = ModelEvaluation(model_eval_entity)
        model_eval_component.evaluation()
        model_eval_component.save_score()
