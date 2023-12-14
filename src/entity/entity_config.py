from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class ConfigDataIngest:
    data_folder : Path
    dataset_name: str

@dataclass(frozen = True)
class ConfigPreprocess():
    data_folder : Path
    Augmentation: bool
    Image_Size: int