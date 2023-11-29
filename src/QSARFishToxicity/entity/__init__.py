from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    destination_folder: Path
    filename: str
    miscellaneous_folder: Path

@dataclass(frozen=True)
class DataValidationTrainingConfig:
    root_dir: Path
    good_dir: Path
    bad_dir: Path
    training_source_dir: Path
    file_name: str
    number_of_columns: int
