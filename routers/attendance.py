# routers/attendance.py
from fastapi import APIRouter, HTTPException
from models.attendance import Attendance, AttendanceCreate
from database import db, serialize_attendance
from datetime import datetime
from bson import ObjectId

router = APIRouter(prefix="/api/attendance", tags=["Attendance"])
attendance_collection = db.attendance

# GET all attendance
@router.get("/", response_model=list[Attendance])
async def get_attendance():
    records = []
    async for r in attendance_collection.find():
        records.append(serialize_attendance(r))
    return records

# POST mark attendance (UPSERT per employee+date)
@router.post("/", response_model=Attendance)
async def mark_attendance(data: AttendanceCreate):
    existing = await attendance_collection.find_one({
        "employeeId": data.employeeId,
        "date": data.date
    })

    if existing:
        await attendance_collection.update_one(
            {"_id": existing["_id"]},
            {"$set": {"status": data.status}}
        )
        updated = await attendance_collection.find_one({"_id": existing["_id"]})
        return serialize_attendance(updated)

    record = data.dict()
    record["createdAt"] = datetime.utcnow()
    result = await attendance_collection.insert_one(record)
    new_record = await attendance_collection.find_one({"_id": result.inserted_id})
    return serialize_attendance(new_record)
