import logging

logger = logging.getLogger(__name__)

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

    def search_knowledge(self, query: str) -> Optional[str]:
        """
        Search for a knowledge entry in the community data.
        
        Args:
            query (str): The search query to find the knowledge entry.
        
        Returns:
            Optional[str]: The found knowledge entry or None if not found.
        
        Raises:
            TypeError: If the input query is not a string.
        
        Examples:
            >>> api = NetworkAPI()
            >>> api.search_knowledge("Learn Python")
            'Learn Python'
        """
        # Validate input type
        if not isinstance(query, str):
            logger.error("Search query must be a string")
            raise TypeError("Search query must be a string")
        
        # Clean the search query
        cleaned_query = query.strip()
        
        # Search for the knowledge entry
        for knowledge in self._community_data:
            if cleaned_query in knowledge:
                logger.info(f"Knowledge entry found: '{knowledge}'")
                return knowledge
        
        logger.info("Knowledge entry not found")
        return None
    
    def update_knowledge(self, old_knowledge: str, new_knowledge: str) -> None:
        """Update an existing knowledge entry with new content.

        Args:
            old_knowledge (str): The existing knowledge entry to update.
            new_knowledge (str): The new content to replace the old entry (must contain at least 1 non-whitespace character).

        Raises:
            TypeError: If either input is not a string.
            ValueError: If new_knowledge is empty or whitespace only, or if old_knowledge is not found.

        Examples:
            >>> api = NetworkAPI()
            >>> api.share_knowledge("Learn Python")
            >>> api.update_knowledge("Learn Python", "Learn advanced Python")
            Successfully updated knowledge to 'Learn advanced Python'
        """
        # Validate input types
        if not isinstance(old_knowledge, str) or not isinstance(new_knowledge, str):
            raise TypeError("Both inputs must be strings")
        
        # Clean the new knowledge content
        cleaned_new = new_knowledge.strip()
        if not cleaned_new:
            raise ValueError("The new knowledge content cannot be empty or whitespace only")
        
        try:
            # Find the index of the knowledge entry to be updated
            index = self._community_data.index(old_knowledge)
        except ValueError:
            raise ValueError("The knowledge entry to update was not found")
        
        # Update the knowledge entry with the cleaned new content
        self._community_data[index] = cleaned_new
        print(f"Successfully updated knowledge to '{cleaned_new}'")

    def delete_knowledge(self, knowledge: str) -> None:
        """Delete an existing knowledge entry from the community data.

        Args:
            knowledge (str): The knowledge entry to delete.

        Raises:
            TypeError: If the input is not a string.
            ValueError: If the knowledge entry is not found.

        Examples:
            >>> api = NetworkAPI()
            >>> api.share_knowledge("Learn Python")
            >>> api.delete_knowledge("Learn Python")
            Successfully deleted knowledge: 'Learn Python'
        """
        # Validate input type
        if not isinstance(knowledge, str):
            raise TypeError("Input must be a string")
        
        # Clean the knowledge content
        cleaned_knowledge = knowledge.strip()
        
        # Check if the knowledge entry exists in the community data
        if cleaned_knowledge not in self._community_data:
            raise ValueError("Knowledge entry not found")
        
        # Remove the knowledge entry from the community data
        self._community_data.remove(cleaned_knowledge)
        print(f"Successfully deleted knowledge: '{cleaned_knowledge}'")

    def append_knowledge(self, knowledge: str) -> None:
        """Append new knowledge to an existing entry in the community data.

        Args:
            knowledge (str): The new knowledge to append to an existing entry.

        Raises:
            TypeError: If the input is not a string.
            ValueError: If the knowledge entry is not found.

        Examples:
            >>> api = NetworkAPI()
            >>> api.share_knowledge("Learn Python")
            >>> api.append_knowledge(" and practice regularly")
            Successfully appended knowledge to 'Learn Python and practice regularly'
        """
        # Validate input type
        if not isinstance(knowledge, str):
            raise TypeError("Input must be a string")
        
        # Clean the knowledge content
        cleaned_knowledge = knowledge.strip()
        
        # Check if the knowledge entry exists in the community data
        if not any(entry.startswith(cleaned_knowledge) for entry in self._community_data):
            raise ValueError("Knowledge entry not found")
        
        # Append the new knowledge to the existing entry
        for i, entry in enumerate(self._community_data):
            if entry.startswith(cleaned_knowledge):
                self._community_data[i] = entry + cleaned_knowledge
                print(f"Successfully appended knowledge to '{entry}'")
                break
