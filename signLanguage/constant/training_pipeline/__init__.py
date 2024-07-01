import os

ARTIFACTS_DIR: str = "artifacts"

"""
Data ingestion related constants
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_ZIP_FILE_NAME = "CollectedImages"
GIT_REPO_NAME = "iNeuron-e2eObjectDetection1"
GIT_USER = "SHK2805"
DATA_DOWNLOAD_URL: str = f"https://github.com/{GIT_USER}/{GIT_REPO_NAME}/raw/main/{DATA_ZIP_FILE_NAME}.zip"

"""
Data validation related constants
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE: str = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "valid", "data.yaml"]

"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

MODEL_TRAINER_NO_EPOCHS: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 16

"""
MODEL PUSHER related constant start with MODEL_PUSHER var name
"""
BUCKET_NAME = "sri-sign-lang-2024"
S3_MODEL_NAME = "best.pt"
