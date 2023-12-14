from src.config.configuration_manager import ConfigurationManager
from src.components.ingest_data_component import IngestDataComponent
class IngestDataPipeline:
    def __init__(self):
        pass

    def main(self):
        cm_ingest_data = ConfigurationManager()
        ingest_data_conf = cm_ingest_data.get_ingest_data_config()
        ingest_data_compo = IngestDataComponent(ingest_data_conf)
        ingest_data_compo.download_data_from_source()

        

