import kaggle # used for data downloading
class IngestDataComponent:
    """
    get the configuration required for data ingestion 
    component to perform tasks like downloading the data
    """
    def __init__(self, config_data_ingest) -> None:
        self.config = config_data_ingest
    
    def download_data_from_source(self):
        """
        method uses kaggle library to download the data from 
        url and save it to the data_folder path mentioned in
        config.yaml path
        """
        kaggle.api.dataset_download_files(self.config.dataset_name,self.config.data_folder,
                                     unzip=True)
    
