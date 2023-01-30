
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://ijuser:iloveibm@cluster0.czn3pnl.mongodb.net/?retryWrites=true&w=majority")
db = cluster["song"]
collection = db["song"]

{"_id": 0, "name": "ijuser", "score": 5}

collection.insert_one()
