import os

ARTIFACTS_DIR: str = "artifacts"

"""
Data ingestion related constants
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_DOWNLOAD_URL: str = "https://github.com/SHK2805/iNeuron-e2eObjectDetection1/raw/main/CollectedImages.zip"

"""
Data validation related constants
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE: str = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "valid", "data.yaml"]
