from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file:Path
    alt_source_URL: str

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

@dataclass(frozen=True)
class TrainingModelConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    epoch: int
    batch_size: int
    look_back: int


@dataclass(frozen=True)
class EvaluatingModelConfig:
    root_dir: Path
    data_path: Path
    model_path: Path