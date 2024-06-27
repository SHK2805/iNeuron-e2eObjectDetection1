import os

ARTIFACTS_DIR: str = "artifacts"

"""
Data ingestion related constants
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
ZIP_FILE_NAME = "CollectedImages"
GIT_REPO_NAME = "iNeuron-e2eObjectDetection1"
GIT_USER = "SHK2805"
DATA_DOWNLOAD_URL: str = f"https://github.com/{GIT_USER}/{GIT_REPO_NAME}/raw/main/{ZIP_FILE_NAME}.zip"

"""
Data validation related constants
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE: str = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "valid", "data.yaml"]
