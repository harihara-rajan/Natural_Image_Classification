from dataclasses import dataclass
from pathlib import Path

@dataclass(frozenset = True)
class ConfigDatIngest:
    data_folder : Path

