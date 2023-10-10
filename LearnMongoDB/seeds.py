from pymongo import MongoClient
from pymongo.server_api import ServerApi
import json


client = MongoClient(
    "mongodb+srv://kseniiavoitko:kJwOlfANt8JTrQ1S@kseniia.fbnhbdy.mongodb.net/",
    server_api=ServerApi("1"),
)

db = client.learnMongoDB

collection_currency = db["authors"]

with open("authors.json") as f:
    file_data = json.load(f)

collection_currency.insert_many(file_data)

collection_currency = db["qoutes"]

with open("qoutes.json") as f:
    file_data = json.load(f)

collection_currency.insert_many(file_data)

client.close()
