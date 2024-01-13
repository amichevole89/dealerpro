from bson.objectid import ObjectId
from inventory.api.client import Queries
from pymongo.errors import PyMongoError

class ManufacturerQueries(Queries):
    DB_NAME = "inventory"
    COLLECTION = "manufacturers"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_manufacturer(self, manufacturer):
        return self.collection.insert_one(manufacturer)

    def list_manufacturers(self):
        return self.collection.find()

    def single_manufacturer(self, id):
        return self.collection.find_one({"_id": ObjectId(id)})

    def update_manufacturer(self, id):
        return self.collection.update_one({"_id": ObjectId(id)})

    def patch_manufacturer(self, id):
        return self.collection.update_one({"_id": ObjectId(id)})

    def delete_manufacturer(self, id):
        try:
            deleted = self.collection.delete_one({"_id": ObjectId(id)})
            if deleted.deleted_count == 1:
                raise PyMongoError("Manufacturer not found for deletion")
            return {"message": "Manufacturer deleted successfully"}
        except PyMongoError as e:
            return {"error": str(e)}
