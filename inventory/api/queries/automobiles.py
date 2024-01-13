from pymongo import MongoClient
from bson.objectid import ObjectId
from ..client import Queries

client = MongoClient('localhost', 27017)

class InventoryQueries(Queries):
    DB_NAME = "inventory"
    COLLECTION = "automobiles"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def create_automobile(self, automobile):
        return self.collection.insert_one(automobile)

    def list_automobiles(self ):
        return self.collection.find()

    def single_automobile(self, id):
        return self.collection.find_one({"_id": ObjectId(id)})

    def update_automobile(self, id):
        return self.collection.update_one({"_id": ObjectId(id)})

    def delete_automobile(self, id):
        return self.collection.delete_one({"_id": ObjectId(id)}