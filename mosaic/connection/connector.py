import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Connector:
    def __init__(self, agent):
        self.agent = agent

    def connect(self):
        # Logic to connect the AI agent to the simulation environment.
        logger.info(f"{self.agent} connected to the Infinite Backrooms.")

    def disconnect(self):
        # Logic to disconnect the AI agent.
        logger.info(f"{self.agent} disconnected from the Infinite Backrooms.")
