import logging
import os


def delete_path(name: str):
    if os.path.exists(name):
        os.system(f"rm -rf {name}")
        logging.info(f"Directory {name} removed")
    else:
        logging.warning(f"Directory {name} does not exist")


delete_path("artifacts")
delete_path("log/*")
delete_path("yolov5/runs")
delete_path("data/*.jpg")

