from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class ConfigDataIngest:
    """
    Configuration data class for the "Data Ingestion" stage in the ML pipeline.

    Attributes:
        data_folder (Path): Path to the folder where data will be ingested.
        dataset_name (str): Name of the dataset to be ingested.

    Example Usage:
        # Instantiate ConfigDataIngest with necessary attributes
        ingest_config = ConfigDataIngest(
            data_folder=Path('/path/to/data/folder'),
            dataset_name='username/dataset-name'
        )
    """
    data_folder : Path
    dataset_name: str

@dataclass(frozen=True)
class BaseModelGeneratorEntity:
    """
    Configuration data class for the "Base Model Generator" stage in the ML pipeline.

    Attributes:
        base_model_path (Path): Path to save the base model.
        actual_model_path (Path): Path to save the actual model.
        CLASSES (int): Number of classes in the classification task.
        EPOCHS (int): Number of training epochs.
        BATCH_SIZE (int): Batch size for training.
        LR (float): Learning rate for model training.
        TEST_SIZE (float): Size of the test set.
        IMAGE_SIZE (list): List specifying the dimensions of input images.

    Example Usage:
        # Instantiate BaseModelGeneratorEntity with necessary attributes
        base_model_entity = BaseModelGeneratorEntity(
            base_model_path=Path('/path/to/base/model'),
            actual_model_path=Path('/path/to/actual/model'),
            CLASSES=10,
            EPOCHS=50,
            BATCH_SIZE=32,
            LR=0.001,
            TEST_SIZE=0.2,
            IMAGE_SIZE=[224, 224, 3]
        )
    """
    base_model_path : Path
    actual_model_path : Path
    CLASSES: int 
    EPOCHS: int
    BATCH_SIZE: int
    LR: float
    TEST_SIZE: float
    IMAGE_SIZE: list

@dataclass(frozen=True)
class CALLBACKSENTITY:
    """
    Configuration data class for callback entities used during model training.

    Attributes:
        root_dir (Path): Root directory for saving logs and checkpoints.
        tensorboard_log_dir (Path): Directory for saving TensorBoard logs.
        checkpoint_file_path (Path): Path to save the model checkpoint.

    Example Usage:
        # Instantiate CALLBACKSENTITY with necessary attributes
        callbacks_entity = CALLBACKSENTITY(
            root_dir=Path('/path/to/root/dir'),
            tensorboard_log_dir=Path('/path/to/tensorboard/logs'),
            checkpoint_file_path=Path('/path/to/checkpoint/file')
        )
    """
    root_dir: Path
    tensorboard_log_dir: Path
    checkpoint_file_path: Path 

@dataclass(frozen=True)
class TrainingEntity:
    """
    Configuration data class for the "Model Training" stage in the ML pipeline.

    Attributes:
        root_dir (Path): Root directory for saving trained models and training history.
        actual_model_path (Path): Path to the actual model for training.
        trained_model_path (Path): Path to save the trained model.
        training_data_path (Path): Path to the training dataset.
        params_epochs (int): Number of training epochs.
        params_batch_size (int): Batch size for training.
        params_is_augment (bool): Flag indicating whether data augmentation is enabled.
        params_image_size (list): List specifying the dimensions of input images.
        model_no (int): Model number or identifier.

    Example Usage:
        # Instantiate TrainingEntity with necessary attributes
        training_entity = TrainingEntity(
            root_dir=Path('/path/to/root/dir'),
            actual_model_path=Path('/path/to/actual/model'),
            trained_model_path=Path('/path/to/trained/model'),
            training_data_path=Path('/path/to/training/data'),
            params_epochs=50,
            params_batch_size=32,
            params_is_augment=True,
            params_image_size=[224, 224, 3],
            model_no=1
        )
    """
    root_dir: Path
    actual_model_path : Path
    trained_model_path: Path
    training_data_path: Path
    params_epochs: int
    params_batch_size: int
    params_is_augment: bool
    params_image_size: list
    model_no: int

@dataclass(frozen=True)
class ModelEvaluationEntity:
    """
    Configuration data class for the "Model Evaluation" stage in the ML pipeline.

    Attributes:
        trained_model_path (Path): Path to the trained model for evaluation.
        training_data_path (Path): Path to the evaluation dataset.
        all_params (dict): Dictionary containing all relevant parameters.
        params_batch_size (int): Batch size for evaluation.
        params_image_size (list): List specifying the dimensions of input images.
        model_no (int): Model number or identifier.

    Example Usage:
        # Instantiate ModelEvaluationEntity with necessary attributes
        model_eval_entity = ModelEvaluationEntity(
            trained_model_path=Path('/path/to/trained/model'),
            training_data_path=Path('/path/to/evaluation/data'),
            all_params={'key': 'value'},
            params_batch_size=32,
            params_image_size=[224, 224, 3],
            model_no=1
        )
    """
    trained_model_path: Path
    training_data_path: Path
    all_params: dict
    params_batch_size: int
    params_image_size: list
    model_no: int
