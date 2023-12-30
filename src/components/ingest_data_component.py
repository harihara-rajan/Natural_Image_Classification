import kaggle # used for data downloading
class IngestDataComponent:
    """
    IngestDataComponent is a class designed for downloading and ingesting data from a specified source, such as Kaggle.
    It utilizes the Kaggle API to download files associated with a given dataset and extracts them into a specified data folder.

    Attributes:
        config (ConfigDataIngest): An instance of ConfigDataIngest containing configuration parameters.

    Methods:
        __init__(self, config_data_ingest): Constructor method to initialize IngestDataComponent with a ConfigDataIngest.
        download_data_from_source(self): Downloads and extracts data files from the specified source using the Kaggle API.

    Example Usage:
        # Instantiate ConfigDataIngest with necessary configuration parameters
        ingest_config = ConfigDataIngest(
            dataset_name='username/dataset-name',
            data_folder='path/to/data/folder'
        )

        # Instantiate IngestDataComponent with ConfigDataIngest
        data_ingest_component = IngestDataComponent(ingest_config)

        # Download and ingest data from the specified source
        data_ingest_component.download_data_from_source()
    """
    def __init__(self, config_data_ingest) -> None:
        """
        Initializes the IngestDataComponent with a given ConfigDataIngest.

        Args:
            config_data_ingest (ConfigDataIngest): An instance of ConfigDataIngest containing configuration parameters.
        """
        self.config = config_data_ingest
    
    def download_data_from_source(self):
        """
        Downloads and extracts data files from the specified source using the Kaggle API.
        """
        kaggle.api.dataset_download_files(self.config.dataset_name,self.config.data_folder,
                                     unzip=True)
    
