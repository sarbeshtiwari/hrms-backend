# models/employee.py
from pydantic import BaseModel, EmailStr
from datetime import datetime

class EmployeeBase(BaseModel):
    employeeId: str
    fullName: str
    email: EmailStr
    department: str

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: str
    createdAt: datetime
