from pymongo import MongoClient
from core.singleton import Singleton


class MongoDB(metaclass=Singleton):
    def __init__(self, uri="mongodb://localhost:27017/", db_name="mlqueue"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name: str):
        """
        Get a collection from the database.
        Args:
            collection_name (str): The name of the collection to retrieve.
        Returns:
            Collection: The MongoDB collection object.
        """
        return self.db[collection_name]

    def close(self):
        """
        Close the MongoDB client connection.
        """
        self.client.close()
