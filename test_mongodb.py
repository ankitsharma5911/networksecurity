
from pymongo.mongo_client import MongoClient
from networksecurity.logger import logging

uri = "mongodb+srv://ankit:ankit@cluster0.0n6et.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    logging.info("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)