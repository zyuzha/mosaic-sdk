class NetworkAPI:
    def __init__(self):
        self.community_data = []

    def share_knowledge(self, knowledge):
        self.community_data.append(knowledge)
        print(f"Knowledge shared: {knowledge}")

    def get_community_data(self):
        return self.community_data
