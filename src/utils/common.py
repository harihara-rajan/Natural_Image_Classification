import yaml 
from box import ConfigBox
from pathlib import Path
def read_yaml(path:Path):
    """
    path: Path to Yaml file to be read
    This function reads the yaml file 
    and returns the contents of the yaml file
    as a ConfigBox object    
    """
    with open(path, 'r') as yaml_file:
        content = yaml.safe_load(yaml_file)
    return ConfigBox(content)