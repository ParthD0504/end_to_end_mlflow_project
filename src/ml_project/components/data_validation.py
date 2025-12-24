import os
import urllib.request as request
import zipfile
from ml_project import logger
from ml_project.utils.common import get_size
from pathlib import Path
from ml_project.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            all_schema = self.config.all_schema
            validation_status= True
            
            for col, expected_dtype in all_schema.items():
                if col not in data.columns:
                    validation_status = False
                    logger.info(f"missing column: {col}")
                    break

                actual_dtype = str(data[col].dtype)
                expected_dtype = str(expected_dtype)
                
                if actual_dtype != expected_dtype:
                    validation_status= False
                    logger.info(f"data types is incorrect, required {expected_dtype}, but got {actual_dtype} for {col}")
                    break
            
            extra_cols = set(data.columns) - set(all_schema.keys())
            if extra_cols:
                validation_status =False
                logger.info(f"extra column found: {extra_cols}")
            
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e



