# models/attendance.py
from pydantic import BaseModel
from datetime import datetime
from typing import Literal

AttendanceStatus = Literal["present", "absent"]

class AttendanceCreate(BaseModel):
    employeeId: str
    date: str            # yyyy-mm-dd
    status: AttendanceStatus

class Attendance(AttendanceCreate):
    id: str
    createdAt: datetime
