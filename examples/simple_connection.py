from mosaic.connection.connector import Connector

def main():
    agent_name = "AI Agent 1"
    connector = Connector(agent_name)
    
    connector.connect()
    
if __name__ == "__main__":
    main()
