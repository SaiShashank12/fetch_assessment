from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file:Path
    unzip_dir: Path

@dataclass(frozen=True)
class FeatureengineeringConfig:
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class SplitingDataConfig:
    root_dir: Path
    data_path: Path
    look_back: int
    split:float