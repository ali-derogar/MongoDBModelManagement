from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from bunnet import init_bunnet
from pymongo import MongoClient


# DATABASE_URI = "mongodb://localhost:27017"
# DATABASE_NAME = "DBModelManagement"
# document_models = []


async def initialize_beanie(
    database_uri: str, database_name: str, document_models: list
):
    """
    Initialize the Beanie framework for asynchronous MongoDB operations.

    Args:
        database_uri (str): The MongoDB connection URI, e.g., "mongodb://localhost:27017".
        database_name (str): The name of the MongoDB database to use.
        document_models (list): A list of Beanie document models representing MongoDB collections.

    Returns:
        None

    Example:
    >>> await initialize_beanie("mongodb://localhost:27017", "mydatabase", [User, Account])
    """
    client = AsyncIOMotorClient(database_uri)
    await init_beanie(database=client[database_name], document_models=document_models)


def initialize_bunnet(database_uri: str, database_name: str, document_models: list):
    """
    Initialize the Bunnet framework for synchronous MongoDB operations.

    Args:
        database_uri (str): The MongoDB connection URI, e.g., "mongodb://localhost:27017".
        database_name (str): The name of the MongoDB database to use.
        document_models (list): A list of Bunnet document models representing MongoDB collections.

    Returns:
        None

    Example:
    >>> initialize_bunnet("mongodb://localhost:27017", "mydatabase", [User, Account])
    """
    client = MongoClient(database_uri)
    init_bunnet(database=client[database_name], document_models=document_models)
