from core.sources.base import Source
from core.connectors.openbravo import OpenbravoConnector

from utils.logger import logger


class OpenbravoSource(Source):
    CONNECTOR = OpenbravoConnector

    def parse_data(self, connector, **kwargs):
        raise NotImplementedError

    def process(self, **kwargs):
        conn = self.CONNECTOR.get_instance(**kwargs)
        logger.info('Starting data parsing...')
        return self.parse_data(conn, **kwargs)
