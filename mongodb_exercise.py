import pymongo

client = pymongo.MongoClient()
db = client["test"]
collection = db["students"]
collection.drop()  # drop the table
collection.insert_one({"id": 123, "name": "zhangsan", "gender": "M", "age": 18})
collection.insert_one({"id": 124, "name": "lisi", "gender": "F", "age": 17})
for item in collection.find():
    print(item)

collection.update_many({"age": 18}, {"$inc": {"age": 2}})

for item in collection.find():
    print(item)

collection.insert_one({"abc": 123})
collection.delete_one({"abc": 123})

res = collection.delete_many({"age": {"$exists": True}})  # 根据是否存在字段

res.deleted_count
