from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.bqccst0.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

student_lists = students.find({})

for doc in student_lists:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")

Bill = students.find_one({"student_id": "1008"})

print("  Student ID: " + Bill["student_id"] + "\n  First Name: " + Bill["first_name"] + "\n  Last Name: " + Bill["last_name"] + "\n")

input("\n\n  End of program, press any key to exit... ")