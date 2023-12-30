from src.config.configuration_manager import ConfigurationManager
from src.components.ingest_data_component import IngestDataComponent
class IngestDataPipeline:
    """
    IngestDataPipeline is a class designed to streamline the process of ingesting data from a specified source.
    It uses the ConfigurationManager to retrieve the ingest data configuration,
    instantiates the IngestDataComponent, and executes the data ingestion pipeline.

    Methods:
        __init__(self): Constructor method to initialize the IngestDataPipeline.
        main(self): Main method to execute the data ingestion pipeline.

    Example Usage:
        # Instantiate IngestDataPipeline
        ingest_data_pipeline = IngestDataPipeline()

        # Execute the data ingestion pipeline
        ingest_data_pipeline.main()
    """
    def __init__(self):
        """
        Initializes the IngestDataPipeline.
        """
        pass  # No specific initialization is performed in this class.

    def main(self):
        """
        Main method to execute the data ingestion pipeline.
        Retrieves ingest data configuration, instantiates IngestDataComponent,
        and executes the data ingestion process.
        """
        cm_ingest_data = ConfigurationManager()
        ingest_data_conf = cm_ingest_data.get_ingest_data_config()
        ingest_data_compo = IngestDataComponent(ingest_data_conf)
        ingest_data_compo.download_data_from_source()

        

