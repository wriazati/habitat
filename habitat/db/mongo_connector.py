from typing import List, Dict, Any

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database


class MongoDBConnection:

    # TODO: Set default variables from configuration / env
    def __init__(self, host: str = 'localhost', port: int = 27017, database: str = 'mydatabase', collection: str = 'mycollection') -> None:
        self.client: MongoClient = MongoClient(f"mongodb://{host}:{port}")
        self.db: Database = self.client[database]
        self.collection: Collection = self.db[collection]

    def insert_document(self, document: Dict[str, Any]) -> None:
        self.collection.insert_one(document)

    def insert_many(self, documents: List[Dict[str, Any]]) -> None:
        if len(documents) > 0:
            self.collection.insert_many(documents)

    def find_documents(self, query: Dict[str, Any]) -> Any:
        return self.collection.find(query)

    def close_connection(self) -> None:
        self.client.close()
