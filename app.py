# print("Om SaiRam")
from signLanguage.logger import logging
from signLanguage.pipeline.training_pipeline import TrainPipeline


logging.info("Welcome to the Sign Language Detection")
train_pipeline = TrainPipeline()
train_pipeline.run_pipeline()
