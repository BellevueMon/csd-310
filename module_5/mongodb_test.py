from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.bqccst0.mongodb.net/pytech"

client = MongoClient(url)

db = client.pytech

print("\n -- Pytech Collection List --")
print(db.list_collection_names())


input("\n\n  End of program, press any key to exit... ")