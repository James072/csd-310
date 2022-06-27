from pymongo import MongoClient

try:
    conn = MongoClient("mongodb+srv://admin:admin@cluster0.mbap3.mongodb.net/?retryWrites=true&w=majority")
    print("Connection active")
    print()
except:
    print("No connection found!")

db = conn.pytech
students = db.students
docs = db.students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print("Student ID: " + doc["student_id"])
    print("First Name: " + doc["first_name"])
    print("Last Name: " + doc["last_name"])
print()

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")
doc = db.students.find_one({"student_id": "1007"})
print()
print("Student ID: " + doc["student_id"])
print("First Name: " + doc["first_name"])
print("Last Name: " + doc["last_name"])
print()
