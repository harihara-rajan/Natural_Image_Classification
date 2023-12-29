from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class ConfigDataIngest:
    data_folder : Path
    dataset_name: str

@dataclass(frozen=True)
class BaseModelGeneratorEntity:
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
    root_dir: Path
    tensorboard_log_dir: Path
    checkpoint_file_path: Path 

@dataclass(frozen=True)
class TrainingEntity:
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
    trained_model_path: Path
    training_data_path: Path
    all_params: dict
    params_batch_size: int
    params_image_size: list
    model_no: int
