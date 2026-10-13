from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/",
                     serverSelectionTimeoutMS=3000)
databases = client.list_database_names()
for database in databases:
    print(database, client[database].list_collection_names())
client.close()