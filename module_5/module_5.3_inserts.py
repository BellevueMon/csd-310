from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.bqccst0.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client["pytech"]

pytech = db["students"]

records = [
    {
        "student_id": "1007",
        "first_name": "Edward",
        "last_name": "Barnes"
    },
    {
        "student_id": "1008",
        "first_name": "Jack",
        "last_name": "Minzer"
    },
    {
        "student_id": "1009",
        "first_name": "Jake",
        "last_name": "Cook"
        
    }
]

for record in records:
    new_student_Id = pytech.insert_one(record).inserted_id
    print(new_student_Id)
    
docs = pytech.find()

for doc in docs:
    print(doc)
    
print(pytech.find_one({"student_id": "1008"}))

input("\n\n  End of program, press any key to exit... ")