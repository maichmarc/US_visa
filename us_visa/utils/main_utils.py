import os
import sys

from us_visa.logger.logger import logging
from us_visa.exception.exception import CustomException

import dill
import yaml
import pandas as pd
import numpy as np




def read_yaml_file(file_path):
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise CustomException(e, sys)
    

def write_yaml_file(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            yaml.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def save_numpy_array_data(file_path, array):
    '''
    Save numpy array data to file
    file_path: str location of file to save
    array: array data to save
    '''
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)

    except Exception as e:
        raise CustomException(e, sys)
    
def load_numpy_array_data(file_path):
    '''
    load numpy array data to file
    file_path: str location of file to save
    array: array data to save
    '''
    try:
       
        with open(file_path, "rb") as file_obj:
            np.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)