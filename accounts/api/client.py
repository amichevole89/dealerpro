from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost:27017/'
client = MongoClient(MONGO_URI)

class Queries:
    @property
    def collection(self):
        db = client[self.DB_NAME]
        return db[self.COLLECTION]
