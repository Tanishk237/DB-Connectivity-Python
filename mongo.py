from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv
load_dotenv()


uri = getenv("MONGO_DB_URL")

client = MongoClient(uri)
try:
    database = client.get_database("new")
    collection = database.get_collection("first")
    query = { "name": "geeksforgeeks" }
    movie = collection.find_one(query)
    print(movie)
    client.close()
except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
