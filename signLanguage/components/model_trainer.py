import os
import sys

import yaml

from signLanguage.constant.training_pipeline import DATA_ZIP_FILE_NAME
from signLanguage.entity.artifacts_entity import ModelTrainerArtifact
from signLanguage.entity.config_entity import ModelTrainerConfig
from signLanguage.exception import SignException
from signLanguage.logger import logging
from signLanguage.utils.main_utils import read_yaml_file


class ModelTrainer:
    def __init__(
            self,
            model_trainer_config: ModelTrainerConfig,
    ):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self, ) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            # get the number of classes from the data.yaml
            # update the custom model yaml file with that data
            logging.info("Unzipping and removing data zip file")
            os.system(f"unzip {DATA_ZIP_FILE_NAME}")
            # os.system(f"rm {DATA_ZIP_FILE_NAME}")

            # get the number of classes from the data.yaml file
            with open("data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])

            # get the model that we are using
            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            logging.info(model_config_file_name)

            # change the default classes in the yolo weights file to the classes in our data
            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")
            config['nc'] = int(num_classes)

            with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)

            os.system("cp -r train yolov5/")
            os.system("cp -r test yolov5/")
            os.system("cp -r valid yolov5/")

            # having issues with automatically writing the number of classes
            # hardcoded manually in a new config file ./models/my_custom_yolov5s.yaml
            os.system(
                f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_{model_config_file_name}.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results  --cache")

            os.system("cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/")
            logging.info(f"Results copied from yolov5/runs/train/yolov5s_results/weights/best.pt to yolov5/")

            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(
                f"cp yolov5/runs/train/yolov5s_results/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")
            logging.info(f"Results copied from yolov5/runs/train/yolov5s_results/weights/best.pt to {self.model_trainer_config.model_trainer_dir}/")

            os.system("rm -rf yolov5/runs")
            os.system("rm -rf train")
            os.system("rm -rf test")
            os.system("rm -rf valid")
            os.system("rm -rf yolov5/train")
            os.system("rm -rf yolov5/test")
            os.system("rm -rf yolov5/valid")
            os.system("rm -rf data.yaml")
            macosx_directory_path = "__MACOSX"
            if os.path.exists(macosx_directory_path):
                os.system(f"rm -rf {macosx_directory_path}")
                logging.info(f"Directory {macosx_directory_path} removed")
            else:
                logging.warning(f"Directory {macosx_directory_path} does not exist")

            logging.info(f"Removed yolov5/runs, train, test, valid folders")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov5/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            raise SignException(e, sys)
