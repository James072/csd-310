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

Storm = {
    "student_id": "1010",
    "first_name": "Johnny",
    "last_name": "Storm"
}

Storm_student_id = students.insert_one(Storm).inserted_id

print("-- INSERT STATEMENTS --")
print(f"\nInserted student record {Storm['first_name']} {Storm['last_name']} into the students collection with document_id {Storm_student_id}")
print()

docs_2 = db.students.find({})
print("-- DISPLAYING NEW STUDENT LIST DOC --")
for doc in docs_2:
    print("Student ID: " + doc["student_id"])
    print("First Name: " + doc["first_name"])
    print("Last Name: " + doc["last_name"])
print()

outcome = db.students.delete_one({"student_id": "1010"})
docs_3 = db.students.find({})

print("-- DELETED STUDENT ID: 1010 --")
for doc in docs_3:
    print("Student ID: " + doc["student_id"])
    print("First Name: " + doc["first_name"])
    print("Last Name: " + doc["last_name"])
print()