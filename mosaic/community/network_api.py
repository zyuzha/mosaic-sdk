class NetworkAPI:
    """A class to manage knowledge sharing within a community network.
    
    Attributes:
        _community_data (list[str]): Private list storing community knowledge entries
    """
    
    def __init__(self) -> None:
        """Initialize NetworkAPI with empty community data storage"""
        self._community_data = []

    def share_knowledge(self, knowledge: str) -> None:
        """Share new knowledge with the community
        
        Args:
            knowledge (str): Knowledge to be shared (minimum 1 character after cleaning)
            
        Raises:
            TypeError: If input is not a string
            ValueError: If input is empty or contains only whitespace
            RuntimeError: If failed to store knowledge
            
        Examples:
            >>> api = NetworkAPI()
            >>> api.share_knowledge("Python best practices")
            Successfully shared knowledge: 'Python best practices'
        """
        try:
            # Validate input type
            if not isinstance(knowledge, str):
                raise TypeError("Input must be a string")
            
            # Clean and validate content
            cleaned_knowledge = knowledge.strip()
            if not cleaned_knowledge:
                raise ValueError("Knowledge cannot be empty or whitespace only")
            
            # Store the knowledge
            self._community_data.append(cleaned_knowledge)
            print(f"Successfully shared knowledge: '{cleaned_knowledge}'")
            
        except Exception as e:
            raise RuntimeError(f"Knowledge sharing failed: {str(e)}") from e

    def get_community_data(self) -> list[str]:
        """Retrieve a safe copy of community knowledge
        
        Returns:
            list[str]: Copy of community data to prevent direct modification
        """
        return self._community_data.copy()

    def clear_community_data(self) -> None:
        """Reset the community knowledge base"""
        self._community_data.clear()
        print("Community data storage has been reset")

    def search_knowledge(self, keyword: str) -> list[str]:
        """Search for knowledge entries containing a keyword
        
        Args:
            keyword (str): Search term (case-insensitive)
            
        Returns:
            list[str]: Matching knowledge entries
            
        Raises:
            TypeError: If keyword is not a string
        """
        if not isinstance(keyword, str):
            raise TypeError("Keyword must be a string")
            
        return [entry for entry in self._community_data if keyword.lower() in entry.lower()]