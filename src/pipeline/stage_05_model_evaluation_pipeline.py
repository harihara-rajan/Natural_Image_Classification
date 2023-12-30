from src.config.configuration_manager import ConfigurationManager
from src.components.stage_05_model_evaluation_component import ModelEvaluation
class ModelEvaluationPipeline:
    """
    ModelEvaluationPipeline is a class designed to streamline the process of evaluating a deep learning model.
    It uses the ConfigurationManager to retrieve model evaluation configuration, instantiates the ModelEvaluation component,
    performs the evaluation, and saves the evaluation scores.

    Methods:
        __init__(self): Constructor method to initialize the ModelEvaluationPipeline.
        main(self) -> None: Main method to execute the model evaluation pipeline.

    Example Usage:
        # Instantiate ModelEvaluationPipeline
        evaluation_pipeline = ModelEvaluationPipeline()

        # Execute the model evaluation pipeline
        evaluation_pipeline.main()
    """
    def __init__(self):
        """
        Initializes the ModelEvaluationPipeline.
        """
        pass # No specific initialization is performed in this class.
    def main()->None:
        """
        Main method to execute the model evaluation pipeline.
        Retrieves model evaluation configuration, instantiates ModelEvaluation component,
        performs the evaluation, and saves the evaluation scores.
        """
        cm = ConfigurationManager()
        model_eval_entity = cm.get_model_evaluation_entity()
        model_eval_component = ModelEvaluation(model_eval_entity)
        model_eval_component.evaluation()
        model_eval_component.save_score()
