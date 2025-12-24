import os
import pandas as pd
from ml_project import logger
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path
from ml_project.components.data_transformation import DataTransformation
from ml_project.config.configuration import ConfigurationManager


STAGE_NAME = "Data Transformation Stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config= config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("data schema is invalid")
            
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try: 
        logger.info(f">>>> stage {STAGE_NAME} <<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.exception(e)
        raise e