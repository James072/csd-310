from pymongo import MongoClient

try:
    conn = MongoClient("mongodb+srv://admin:admin@cluster0.mbap3.mongodb.net/?retryWrites=true&w=majority")
    print("Connection active")
    print()
except:
    print("No connection found!")

db = conn.pytech
students = db.students

Parker = {
    "student_id": "1007", 
    "first_name": "Peter",
    "last_name": "Parker"
}

Parker_student_id = students.insert_one(Parker).inserted_id

Drake = {
    "student_id": "1008",
    "first_name": "Bobby",
    "last_name": "Drake"
}

Drake_student_id = students.insert_one(Drake).inserted_id

Khan = {
    "student_id": "1009",
    "first_name": "Kamala",
    "last_name": "Khan"
}

Khan_student_id = students.insert_one(Khan).inserted_id

print("-- INSERT STATEMENTS --")
print(f"\nInserted student record {Parker['first_name']} {Parker['last_name']} into the students collection with document_id {Parker_student_id}")
print(f"\nInserted student record {Drake['first_name']} {Drake['last_name']} into the students collection with document_id {Drake_student_id}")
print(f"\nInserted student record {Khan['first_name']} {Khan['last_name']} into the students collection with document_id {Khan_student_id}")
print()