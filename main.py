import json

from habitat.data_ingestion.eso_data_downloader import EsoDownloader
from habitat.db.mongo_connector import MongoDBConnection
import argparse

# Create the argument parser
parser = argparse.ArgumentParser(description='Data Download and Print')

# Add the command line arguments
parser.add_argument('-d', '--download', action='store_true', help='Enable downloading for today')
parser.add_argument('-p', '--print', action='store_true', help='Print current data')
parser.add_argument('-c', '--clear', action='store_true', help='Clear DB')
parser.add_argument('-q', '--query', type=str, help='Query DB with a filter')

# Parse the command line arguments
args = parser.parse_args()

# Init clients
eso = EsoDownloader()
connection = MongoDBConnection()

if args.download:
    print('Downloading data...')
    data = eso.download()
    connection.insert_many(data)
    print('Data downloaded successfully.')

if args.print:
    print('Printing data from db...')
    query = json.loads(args.query) if args.query else None
    cursor = connection.collection.find(query)
    for document in cursor:
        print(document)

if args.clear:
    print('Clearing data from db...')
    connection.collection.drop()

# Close conn
connection.close_connection()
