import logging
import os


def delete_folder(name: str):
    if os.path.exists(name):
        os.system(f"rm -rf {name}")
        logging.info(f"Directory {name} removed")
    else:
        logging.warning(f"Directory {name} does not exist")


delete_folder("artifacts")
