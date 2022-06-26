from pymongo import MongoClient


url = "mongodb+srv://admin:admin@cluster0.mbap3.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

id = {"Student ID": "1007"}
new_student_id = students.insert_one(id).inserted_id
print(new_student_id)