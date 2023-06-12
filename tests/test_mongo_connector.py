import unittest
from pymongo import MongoClient

# Import the class to be tested
from habitat.db.mongo_connector import MongoDBConnection

class MongoDBConnectionTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a test database and collection
        cls.test_client = MongoClient()
        cls.test_db = cls.test_client['testdatabase']
        cls.test_collection = cls.test_db['testcollection']

    @classmethod
    def tearDownClass(cls):
        # Drop the test collection and database
        cls.test_collection.drop()
        cls.test_db.client.drop_database(cls.test_db)

    def setUp(self):
        # Create an instance of MongoDBConnection for each test case
        self.connection = MongoDBConnection(database='testdatabase', collection='testcollection')

    def tearDown(self):
        # Drop all documents from the test collection after each test case
        self.test_collection.delete_many({})
        self.connection.close_connection()

    def test_find_documents(self):
        document1 = {"name": "John", "age": 30}
        document2 = {"name": "Jane", "age": 25}
        self.connection.insert_document(document1)
        self.connection.insert_document(document2)

        query = {"name": "John"}
        result = self.connection.find_documents(query)
        documents = list(result)

        self.assertEqual(len(documents), 1)
        self.assertEqual(documents[0]["name"], "John")

if __name__ == '__main__':
    unittest.main()
