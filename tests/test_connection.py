import unittest
import logging
from mosaic.connection.connector import Connector

class TestConnector(unittest.TestCase):
    def setUp(self):
        self.agent_name = "Test Agent"
        self.connector = Connector(self.agent_name)
        # Set up logging to capture output for testing
        self.logger = logging.getLogger('mosaic.connection.connector')
        self.logger.setLevel(logging.INFO)
        self.log_stream = logging.StreamHandler()
        self.log_stream.setLevel(logging.INFO)
        self.logger.addHandler(self.log_stream)

    def tearDown(self):
        # Remove the log handler after tests
        handlers = self.logger.handlers[:]
        for handler in handlers:
            self.logger.removeHandler(handler)

    def test_connect(self):
        with self.assertLogs(self.logger, level='INFO') as log:
            self.connector.connect()
            # Adjust assertion to match the actual log format
            self.assertIn(f'INFO:mosaic.connection.connector:{self.agent_name} connected to the Infinite Backrooms.', log.output)

    def test_disconnect(self):
        with self.assertLogs(self.logger, level='INFO') as log:
            self.connector.disconnect()
            # Adjust assertion to match the actual log format
            self.assertIn(f'INFO:mosaic.connection.connector:{self.agent_name} disconnected from the Infinite Backrooms.', log.output)

if __name__ == '__main__':
    unittest.main()
