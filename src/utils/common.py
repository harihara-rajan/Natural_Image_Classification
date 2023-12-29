import os
import yaml 
from box import ConfigBox
import json
from pathlib import Path
from src.logger import logging
def read_yaml(path:Path):
    """
    path: Path to Yaml file to be read
    This function reads the yaml file 
    and returns the contents of the yaml file
    as a ConfigBox object    
    """
    with open(path, 'r') as yaml_file:
        content = yaml.safe_load(yaml_file)
        logging.info(f'Read yaml file: {path}: Success')
    return ConfigBox(content)

def create_dirs(pathtofile: list):
    for path in pathtofile:
        direc_path = os.path.dirname(path)
        os.makedirs(direc_path, exist_ok=True)
        logging.info(f'Created Directory: {os.path.join(os.getcwd(),direc_path)}: Success')

def save_json(values:dict, path:Path)-> None:
    with open(path, 'w') as json_file:
        json.dump(values, json_file)

def write_yaml(values:dict, path:Path):
    with open(path, 'w') as json_file:
        yaml.dump(values, json_file)
