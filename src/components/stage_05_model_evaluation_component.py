import os
from src.config.configuration_manager import ModelEvaluationEntity
import tensorflow as tf
from pathlib import Path
from src.utils.common import save_json, create_dirs

class ModelEvaluation:
    """
    ModelEvaluation is a class designed for evaluating a trained deep learning model using TensorFlow and Keras.
    It includes functionalities for loading a trained model, preparing a validation data generator, and conducting
    evaluation. The evaluation results are then saved as a JSON file.

    Attributes:
        config (ModelEvaluationEntity): An instance of ModelEvaluationEntity containing configuration parameters.
        valid_data_generator (tf.keras.preprocessing.image.DirectoryIterator): Generator for validation data.
        score (list): Evaluation scores, typically containing loss and accuracy.

    Methods:
        __init__(self, ModelEvaluationEntity): Constructor method to initialize the ModelEvaluation with a ModelEvaluationEntity.
        _valid_generator(self): Prepares the validation data generator based on the provided configuration.
        evaluation(self): Evaluates the trained model using the validation data generator.
        save_score(self): Saves the evaluation scores as a JSON file.

    Example Usage:
        # Instantiate ModelEvaluationEntity with necessary configuration parameters
        evaluation_config = ModelEvaluationEntity(
            trained_model_path='path/to/trained/model.h5',
            training_data_path='path/to/training/data',
            params_image_size=(224, 224, 3),
            params_batch_size=32,
            model_no=1
        )

        # Instantiate ModelEvaluation with the ModelEvaluationEntity
        evaluator = ModelEvaluation(evaluation_config)

        # Evaluate the model and save the scores
        evaluator.evaluation()
        evaluator.save_score()
    """
    def __init__(self, ModelEvaluationEntity):
        self.config = ModelEvaluationEntity
    
    def _valid_generator(self):
        data_preprocessing_kwargs = dict(
            rescale=1./255, 
            validation_split = 0.3
        )
        valid_data_preprocessing = tf.keras.preprocessing.image.ImageDataGenerator(**data_preprocessing_kwargs)
        self.valid_data_generator  = valid_data_preprocessing.flow_from_directory(
            directory = self.config.training_data_path, 
            target_size= self.config.params_image_size[:-1],
            batch_size= self.config.params_batch_size, 
            shuffle=False
        )
    
    @property
    def _load_model(path:Path):  
        print(path)
        return tf.keras.models.load_model(path)
    
    def evaluation(self):
        trained_model_path = os.path.join(
            os.path.dirname(self.config.trained_model_path),
            f"trained_model_{self.config.model_no}.h5")
        # self.model = self._load_model(self.config.trained_model_path)
        model = tf.keras.models.load_model(trained_model_path)
        self._valid_generator()
        self.score = model.evaluate(self.valid_data_generator) # list ["loss", "acc"]
    
    def save_score(self):
        scores = dict(
            loss = self.score[0],
            accuracy = self.score[1]
        )
        path_to_save_scores = os.path.join(os.path.dirname(self.config.trained_model_path), 'scores')
        create_dirs([path_to_save_scores])
        save_json(values= scores, 
                  path=os.path.join(path_to_save_scores,f"training_score_{self.config.model_no}.json"))
        

