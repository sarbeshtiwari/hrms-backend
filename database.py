from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

MONGO_URL = "mongodb+srv://rahul8454454singh_db_user:RTy3kh8TTiwunUQe@cluster0.ln3yg2l.mongodb.net/?appName=hrms"
client = AsyncIOMotorClient(MONGO_URL)
db = client.hrms  # Database name

# Generic helper to convert Mongo document _id to string
# database.py
def serialize_doc(doc):
    return {
        "id": str(doc["_id"]),
        "employeeId": doc["employeeId"],
        "fullName": doc["fullName"],
        "email": doc["email"],
        "department": doc["department"],
        "createdAt": doc["createdAt"],
    }

def serialize_attendance(doc):
    return {
        "id": str(doc["_id"]),
        "employeeId": doc["employeeId"],
        "date": doc["date"],
        "status": doc["status"],
        "createdAt": doc["createdAt"],
    }
