import logging

logger = logging.getLogger(__name__)

class RatingAPI:
    """A class to manage ratings for knowledge entries in the community network."""
    
    def __init__(self, community_data):
        """
        Initialize RatingAPI with a reference to the community data.
        
        Args:
            community_data: The community data instance to operate on.
        """
        self.community_data = community_data
        self.ratings = {}

    def rate_knowledge(self, knowledge: str, rating: int) -> None:
        """
        Rate a knowledge entry.
        
        Args:
            knowledge (str): The knowledge entry to rate.
            rating (int): The rating value (1 to 5).
        
        Raises:
            TypeError: If the knowledge is not a string or rating is not an integer.
            ValueError: If the rating is not between 1 and 5 or knowledge entry is not found.
        """
        if not isinstance(knowledge, str):
            raise TypeError("Knowledge must be a string")
        if not isinstance(rating, int):
            raise TypeError("Rating must be an integer")
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        
        cleaned_knowledge = knowledge.strip()
        if cleaned_knowledge not in self.community_data:
            raise ValueError("Knowledge entry not found")
        
        if cleaned_knowledge not in self.ratings:
            self.ratings[cleaned_knowledge] = []
        
        self.ratings[cleaned_knowledge].append(rating)
        logger.info(f"Rated knowledge '{cleaned_knowledge}' with {rating} stars")

    def get_average_rating(self, knowledge: str) -> float:
        """
        Get the average rating for a knowledge entry.
        
        Args:
            knowledge (str): The knowledge entry to get the average rating for.
        
        Returns:
            float: The average rating.
        
        Raises:
            TypeError: If the knowledge is not a string.
            ValueError: If the knowledge entry is not found or has no ratings.
        """
        if not isinstance(knowledge, str):
            raise TypeError("Knowledge must be a string")
        
        cleaned_knowledge = knowledge.strip()
        if cleaned_knowledge not in self.ratings or not self.ratings[cleaned_knowledge]:
            raise ValueError("Knowledge entry not found or has no ratings")
        
        average_rating = sum(self.ratings[cleaned_knowledge]) / len(self.ratings[cleaned_knowledge])
        logger.info(f"Average rating for '{cleaned_knowledge}' is {average_rating:.2f} stars")
        return average_rating