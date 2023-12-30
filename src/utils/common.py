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
    """
    Creates directories specified in the given list of file paths.

    Args:
        pathtofile (list): List of file paths for which directories need to be created.

    Returns:
        None

    Example Usage:
        # Create directories for a list of file paths
        create_dirs(['/path/to/file1.txt', '/path/to/file2.txt'])
    """
    for path in pathtofile:
        direc_path = os.path.dirname(path)
        os.makedirs(direc_path, exist_ok=True)
        logging.info(f'Created Directory: {os.path.join(os.getcwd(),direc_path)}: Success')

def save_json(values:dict, path:Path)-> None:
    """
    Saves a dictionary as a JSON file.

    Args:
        values (dict): Dictionary to be saved as JSON.
        path (Path): Path to the destination JSON file.

    Returns:
        None

    Example Usage:
        # Save a dictionary as a JSON file
        save_json({'key': 'value'}, Path('/path/to/file.json'))
    """
    with open(path, 'w') as json_file:
        json.dump(values, json_file)

def write_yaml(values:dict, path:Path):
    """
    Writes a dictionary to a YAML file.

    Args:
        values (dict): Dictionary to be written to YAML.
        path (Path): Path to the destination YAML file.

    Returns:
        None

    Example Usage:
        # Write a dictionary to a YAML file
        write_yaml({'key': 'value'}, Path('/path/to/file.yaml'))
    """
    with open(path, 'w') as json_file:
        yaml.dump(values, json_file)
